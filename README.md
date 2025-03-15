# Sticky Notes Application

## Introduction

The Sticky Notes Application is a Python desktop program built with the Tkinter library. It allows users to create, customize, move, and resize virtual sticky notes on their desktop environment. The application persists user data—including note text, color, position, and dimensions—using a JSON configuration file, ensuring that notes are retained across sessions.

## Objectives

- Provide an intuitive interface for creating and managing sticky notes.
- Persist user data via a configuration file (`config.json`).
- Enable customization through a right-click context menu.
- Support dynamic manipulation of notes (dragging, resizing, and color changes).

## Features

- **Dynamic Note Creation:** Easily create new sticky notes with default or user-defined settings.
- **Customization:** Change the background color of each note from a predefined palette.
- **Drag & Drop:** Move notes freely across the screen.
- **Resizing:** Adjust note dimensions dynamically.
- **Persistence:** Automatically save note configurations to `config.json` to maintain state between sessions.
- **Context Menus:** Use context menus for quick access to functions such as note creation, deletion, and customization.
  
![Notitas](https://github.com/foxxfiles/notitas/blob/main/images/notitas.png)

## Installation

### Prerequisites

- Python 3.x (Tkinter is usually included)
- Windows exe binaries (https://github.com/foxxfiles/notitas/blob/main/dist/notitas.exe)
### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/foxxfiles/notitas
   cd notityas
   python notitas.py


## Disclaimer / Aviso Legal

This software is provided "as is", without any express or implied warranties, including, but not limited to, the warranties of merchantability or fitness for a particular purpose. Fernando Aberto Velasquez Aguilera shall not be held liable for any damages or losses arising from the use or inability to use this software. Users assume full responsibility for testing and verifying the software's suitability for their intended purposes prior to deployment in any production environment. Use of this software is entirely at your own risk. For any commercial modifications or implementations, it is strongly recommended to seek independent legal counsel.

El software se distribuye "tal cual", sin garantías expresas o implícitas, incluyendo, entre otras, las garantías de comerciabilidad o idoneidad para un propósito específico. Fernando Aberto Velasquez Aguilera no se hace responsable de los daños o perjuicios derivados del uso o de la imposibilidad de uso del software. El usuario asume la responsabilidad completa de probar y verificar la idoneidad del software para los fines que pretenda, antes de emplearlo en entornos de producción. El uso del software es completamente bajo su propio riesgo. Se recomienda encarecidamente buscar asesoramiento legal independiente para cualquier modificación o implementación comercial.
