from tkinter import *
from tkinter import ttk
# CUSTOM SCRIPTS
from VIEW import file_transfer_gui as gui

def main():
    root = Tk()
    FT = gui.FileTransfer(root)
    root.mainloop()

if __name__ == '__main__': main()