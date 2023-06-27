import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

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
        messagebox.showinfo("Success", "Files renamed successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")


def browse_directory():
    directory = filedialog.askdirectory(title='Select Directory')
    if directory:
        directory_label.configure(text=directory)


def cancel_program():
    if messagebox.askyesno("Cancel", "Are you sure you want to cancel?"):
        root.destroy()


root = tk.Tk()
root.title("Simple Batch Image File Renamer")
root.geometry("450x190")

# Create GUI elements
directory_frame = tk.Frame(root)
directory_frame.pack(pady=10)

directory_label = tk.Label(directory_frame, text="No directory selected", wraplength=400)
directory_label.pack(side=tk.LEFT)

browse_button = tk.Button(directory_frame, text="Browse", command=browse_directory)
browse_button.pack(side=tk.LEFT, padx=(10, 0))

entry_frame = tk.Frame(root)
entry_frame.pack()

entry_label = tk.Label(entry_frame, text="Enter prefix for file names:")
entry_label.pack(side=tk.LEFT)

entry = tk.Entry(entry_frame)
entry.pack(side=tk.LEFT, padx=(20, 0))

rename_button = tk.Button(root, text="Rename Files", height= 2, width= 30, command=lambda: rename_files(directory_label.cget("text")))
rename_button.pack(pady=10)

cancel_button = tk.Button(root, text="Cancel", height= 1, width= 30, command=cancel_program)
cancel_button.pack(pady=10)

root.mainloop()
