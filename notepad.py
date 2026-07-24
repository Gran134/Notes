import tkinter as tk

root = tk.Tk()
root.title("Notepad")

def new_file():
    print("New File")

def open_file():
    print("Open File")

def save_file():
    print("Save File")

def save_as():
    print("Save As")

# Create the menu bar
menubar = tk.Menu(root)

# Create the File menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New File", command=new_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)

# Add "File" to the menu bar
menubar.add_cascade(label="File", menu=file_menu)

# Display the menu bar
root.config(menu=menubar)

root.mainloop()
