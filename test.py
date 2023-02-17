import tkinter as tk
from tkinter import filedialog

def browse_file(entry):
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

def add_entry():
    entry_frame = tk.Frame(scrollable_frame)
    entry_frame.pack(side="top", padx=10, pady=10, fill="x")
    
    # Add checkbox to the left of the entry
    check_var = tk.BooleanVar()
    check_button = tk.Checkbutton(entry_frame, variable=check_var)
    check_button.pack(side="left")
    
    # Add entry widget
    entry = tk.Entry(entry_frame, width=40)
    entry.pack(side="left")
    
    # Add "Browse" button in between the entry and size columns
    browse_button = tk.Button(entry_frame, text="Browse", command=lambda e=entry: browse_file(e))
    browse_button.pack(side="left", padx=10)
    
    # Add label widgets to show size and file count
    size_label = tk.Label(entry_frame, text="0 B")
    size_label.pack(side="right", padx=10)
    files_label = tk.Label(entry_frame, text="0 files")
    files_label.pack(side="right", padx=10)
    
    entries.append((check_var, entry, browse_button, size_label, files_label))

def add_column_headers():
    header_frame = tk.Frame(scrollable_frame)
    header_frame.pack(side="top", padx=10, pady=10, fill="x")
    
    # Add checkbox header
    check_header_var = tk.BooleanVar()
    check_header = tk.Checkbutton(header_frame, variable=check_header_var)
    check_header.pack(side="left")
    
    # Add path header
    path_header = tk.Label(header_frame, text="Path")
    path_header.pack(side="left", padx=10)
    
    # Add size header
    size_header = tk.Label(header_frame, text="Size")
    size_header.pack(side="right", padx=10)
    
    # Add files header
    files_header = tk.Label(header_frame, text="Files")
    files_header.pack(side="right", padx=10)

root = tk.Tk()
root.title("Backup")
entries = []

# Create a canvas and a scrollbar
canvas = tk.Canvas(root, width=600, height=400)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)


canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

add_button = tk.Button(scrollable_frame, text="Add entry", command=add_entry)
add_button.pack(anchor= "w", side="bottom", padx=10, pady=10)


add_column_headers()
add_entry()

root.mainloop()
