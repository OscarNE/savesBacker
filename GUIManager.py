import tkinter as tk
from tkinter import filedialog

class GUIManager:

  def __init__(self):
    self.saveEntries = []
    self.addEntryButton = "" #TODO
    self.applyButton = "" #TODO
    self.cancelButton = "" #TODO


def browse_file(entry):
    file_path = filedialog.askdirectory(initialdir = "/", title = "Select path")
    entry.insert(0, file_path)

def initGUI():
    root = tk.Tk()
    root.title("Backup")
    root.geometry("500x200")

    entry = tk.Entry(root)
    entry.grid(row=0, column=0, padx=10, pady=10)

    browse_button = tk.Button(root, text="Browse", command=browse_file(entry))
    browse_button.grid(row=0, column=1, padx=10, pady=10)

    root.mainloop()