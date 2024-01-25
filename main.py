from tkinter import *
import minesw


root = Tk()
root.option_add("*tearOff", False)

main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label="New", command=lambda: minesw.Game(7,7,2))
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit")

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="View")

root.config(menu=main_menu)

root.mainloop()