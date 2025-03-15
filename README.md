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
![Descripción de la imagen](https://example.com/path/to/image.png)
## Installation

### Prerequisites

- Python 3.x (Tkinter is usually included)
- (Optional) A virtual environment for dependency management

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/foxxfiles/notitas
   cd notityas
   python notitas.py
