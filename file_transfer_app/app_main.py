from tkinter import *
from tkinter import ttk
# CUSTOM SCRIPTS
from VIEW import file_transfer_gui as gui
from MODEL import file_transfer_init_schema as schema

def main():
    root = Tk()
    FT = gui.FileTransfer(root)
    schema.createDb()
    root.mainloop()

if __name__ == '__main__': main()