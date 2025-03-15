"""
Copyright (c) 2025 Fernando Aberto Velasquez Aguilera.
Licensed under the MIT License with Commons Clause.
See the LICENSE file for details.
"""

import tkinter as tk
from tkinter import ttk
import json
import os

CONFIG_FILE = "config.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        default_colors = ["#FFB3BA", "#FFDFBA", "#FFFFBA", "#BFFFBF", "#BAFFFF", 
                          "#BACDFF", "#F3BAFF", "#FFBAF7", "#FFBACD", "#FFD700"]
        default_config = {
            "notes": [],
            "default_width": 250,
            "default_height": 200,
            "colors": default_colors
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(default_config, f)
    
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)
    
    for note in config.get("notes", []):
        note.setdefault("text", "")
        note.setdefault("color", "#FFDFBA")
        note.setdefault("x", 100)
        note.setdefault("y", 100)
        note.setdefault("width", config.get("default_width", 250))
        note.setdefault("height", config.get("default_height", 200))
    
    return config

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def create_color_image(color):
    # Crear una imagen pequeña de 20x20 con el color indicado
    img = tk.PhotoImage(width=20, height=20)
    img.put(color, to=(0, 0, 20, 20))
    return img

class StickyNotesApp:
    def __init__(self):
        self.config = load_config()
        self.notes_windows = []
        self.colors = self.config.get("colors", ["#FFB3BA", "#FFDFBA", "#FFFFBA", "#BFFFBF", "#BAFFFF", 
                                                  "#BACDFF", "#F3BAFF", "#FFBAF7", "#FFBACD", "#FFD700"])
        # Crear imagenes para mostrar los colores en el menu
        self.color_images = {}
        self.root = tk.Tk()
        # Es importante crear las imagenes despues de inicializar la ventana principal
        for c in self.colors:
            self.color_images[c] = create_color_image(c)
        self.default_width = self.config.get("default_width", 250)
        self.default_height = self.config.get("default_height", 200)
        self.root.withdraw()
        if not self.config["notes"]:
            self.create_default_note()
        else:
            for note in self.config["notes"]:
                self.create_note(note["text"], note["color"], note["x"], note["y"], note["width"], note["height"])
        self.global_context_menu = tk.Menu(self.root, tearoff=0)
        self.global_context_menu.add_command(label="Crear nueva nota", command=self.add_new_note)
        self.global_context_menu.add_separator()
        self.global_context_menu.add_command(label="Salir de la aplicacion", command=self.on_close)
        self.root.bind("<Button-3>", self.show_global_context_menu)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_default_note(self):
        default_color = self.colors[0]
        x, y = self.root.winfo_screenwidth() // 2, self.root.winfo_screenheight() // 2
        self.create_note("Bienvenido a tus notas!", default_color, x, y, self.default_width, self.default_height)
        self.config["notes"].append({
            "text": "Bienvenido a tus notas!", 
            "color": default_color, 
            "x": x, "y": y, 
            "width": self.default_width, 
            "height": self.default_height
        })

    def create_note(self, text_content="", color=None, x=100, y=100, width=None, height=None):
        if not color:
            color = self.colors[len(self.notes_windows) % len(self.colors)]
        if width is None:
            width = self.default_width
        if height is None:
            height = self.default_height
        note_window = tk.Toplevel()
        note_window.overrideredirect(True)
        note_window.geometry(f"{width}x{height}+{x}+{y}")
        note_window.wm_attributes("-topmost", 1)
        note_window.configure(bg=color)
        text = tk.Text(note_window, bg=color, fg="black", wrap='word',
                       padx=10, pady=10, borderwidth=0, insertbackground="black")
        text.insert('1.0', text_content)
        text.pack(fill='both', expand=True)
        
        # Crear menu contextual para la nota
        context_menu = tk.Menu(note_window, tearoff=0)
        context_menu.add_command(label="Cerrar nota", command=lambda: self.close_note(note_window))
        context_menu.add_command(label="Destruir nota", command=lambda: self.destroy_note(note_window))
        # Configurar un submenu de colores personalizado
        submenu_colores = tk.Menu(context_menu, tearoff=0)
        # Configurar el menu para minimizar espacios
        submenu_colores.config(borderwidth=0, activeborderwidth=0)
        
        for c in self.colors:
            submenu_colores.add_command(
                label="",
                image=self.color_images[c],
                compound="center",
                background=c,
                activebackground=c,
                command=lambda color=c: self.change_note_color(note_window, text, color)
            )
        context_menu.add_cascade(label="Colores", menu=submenu_colores)
        context_menu.add_separator()
        context_menu.add_command(label="Crear nueva nota", command=self.add_new_note)
        context_menu.add_separator()
        context_menu.add_command(label="Salir de la aplicacion", command=self.on_close)
        
        def show_context_menu(event):
            try:
                context_menu.tk_popup(event.x_root, event.y_root)
            finally:
                context_menu.grab_release()
        
        note_window.bind("<Button-3>", show_context_menu)
        self.setup_drag(note_window)
        self.setup_resize(note_window)
        self.notes_windows.append((note_window, text))

    def change_note_color(self, note_window, text_widget, new_color):
        note_window.configure(bg=new_color)
        text_widget.configure(bg=new_color)
        for i, (w, t) in enumerate(self.notes_windows):
            if w == note_window:
                self.config["notes"][i]["color"] = new_color
                break
        save_config(self.config)

    def add_new_note(self):
        new_color = self.colors[len(self.notes_windows) % len(self.colors)]
        x, y = self.root.winfo_pointerx(), self.root.winfo_pointery()
        self.create_note(color=new_color, x=x, y=y, width=self.default_width, height=self.default_height)
        self.config["notes"].append({
            "text": "", 
            "color": new_color, 
            "x": x, "y": y, 
            "width": self.default_width, 
            "height": self.default_height
        })

    def close_note(self, note_window):
        note_window.withdraw()
        self.check_all_notes_closed()

    def destroy_note(self, note_window):
        for i, (window, _) in enumerate(self.notes_windows):
            if window == note_window:
                self.config["notes"].pop(i)
                self.notes_windows.pop(i)
                break
        note_window.destroy()
        save_config(self.config)
        if not self.notes_windows:
            self.on_close()

    def check_all_notes_closed(self):
        all_closed = all(not window.winfo_viewable() for window, _ in self.notes_windows)
        if all_closed:
            self.on_close()

    def setup_drag(self, window):
        window.bind("<ButtonPress-1>", lambda event: self.start_drag(event, window))
        window.bind("<B1-Motion>", lambda event: self.on_drag(event, window))

    def start_drag(self, event, window):
        self._x = event.x
        self._y = event.y

    def on_drag(self, event, window):
        x = window.winfo_x() + (event.x - self._x)
        y = window.winfo_y() + (event.y - self._y)
        window.geometry(f"+{x}+{y}")

    def setup_resize(self, window):
        resize_zone = tk.Frame(window, bg="#000000", width=10, height=10, cursor="sizing")
        resize_zone.place(relx=1.0, rely=1.0, anchor="se")
        
        def start_resize(event):
            self._start_x = event.x_root
            self._start_y = event.y_root
            self._start_width = window.winfo_width()
            self._start_height = window.winfo_height()
        
        def on_resize(event):
            new_width = self._start_width + (event.x_root - self._start_x)
            new_height = self._start_height + (event.y_root - self._start_y)
            if new_width > 100 and new_height > 100:
                window.geometry(f"{new_width}x{new_height}")
                self.default_width = new_width
                self.default_height = new_height
                self.config["default_width"] = new_width
                self.config["default_height"] = new_height
        
        resize_zone.bind("<ButtonPress-1>", start_resize)
        resize_zone.bind("<B1-Motion>", on_resize)

    def show_global_context_menu(self, event):
        try:
            self.global_context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.global_context_menu.grab_release()

    def on_close(self):
        for i, (window, text) in enumerate(self.notes_windows):
            if window.winfo_viewable():
                self.config["notes"][i]["text"] = text.get("1.0", 'end-1c')
                self.config["notes"][i]["x"] = window.winfo_x()
                self.config["notes"][i]["y"] = window.winfo_y()
                self.config["notes"][i]["width"] = window.winfo_width()
                self.config["notes"][i]["height"] = window.winfo_height()
        save_config(self.config)
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = StickyNotesApp()
    app.run()