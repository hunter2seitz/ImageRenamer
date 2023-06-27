import os
import tkinter as tk
from tkinter import filedialog

# Author Hunter Seitz
# Copyright 2023

def rename_files(directory):
    try:
        file_list = os.listdir(directory)
        prefix = entry.get()
        counter = 1

        image_files = [filename for filename in file_list if filename.lower().endswith(('.jpg', '.jpeg', '.png'))]

        if not image_files:
            raise ValueError("No image files found in the directory.")

        for filename in image_files:
            file_path = os.path.join(directory, filename)
            new_filename = f"{prefix}_{counter}{os.path.splitext(filename)[1]}"

            new_file_path = os.path.join(directory, new_filename)
            os.rename(file_path, new_file_path)

            counter += 1

        entry.delete(0, tk.END)
        status_label.configure(text='Files renamed successfully!')

    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}")


def browse_directory():
    directory = filedialog.askdirectory(title='Select Directory')
    if directory:
        directory_label.configure(text=directory)


def cancel_program():
    root.destroy()


root = tk.Tk()
root.title("Simple Batch Image File Renamer")
root.geometry("450x250")

# Create GUI elements
directory_label = tk.Label(root, text="No directory selected", wraplength=400)
directory_label.pack(pady=10)

browse_button = tk.Button(root, text="Browse", justify= "right", command=browse_directory)
browse_button.pack(pady=10)

entry_label = tk.Label(root, text="Enter prefix for file names:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack(pady=10)

rename_button = tk.Button(root, text="Rename Files", command=lambda: rename_files(directory_label.cget("text")))
rename_button.pack(pady=10)

cancel_button = tk.Button(root, text="Cancel", height= 1, width= 30, command=cancel_program)
cancel_button.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
