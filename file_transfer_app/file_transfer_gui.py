from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import shutil, os
import datetime, time
import file_transfer_controller as ctrl

class FileTransfer:


    def __init__(self, master):

        #MASTER SETTINGS
        master.title('FILE TRANSFER')
        master.resizable(False, False)
        master.configure(background = 'black')

        self.style = ttk.Style()
        #IMAGE
        # CD REMOVED: self.transfer = PhotoImage(file = 'C:\\Users\\Dell 0381\\Desktop\\Python practice\\Custom Projects\\icons\\transfer.png')
        # CD REMOVED: self.icon = self.transfer


        #HEADER
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()

        # CD REMOVED: , image = self.icon
        ttk.Label(self.header_frame).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.header_frame, text = 'A SIMPLE FILE TRANSFER PROGRAM').grid(row = 0, column = 1)
        ttk.Label(self.header_frame, text = 'BROWSE for ROOT and DEST file locations.\n'
                                            'Apply COMMENTS as needed (or required).\n').grid(row = 1, column = 1)



        #CONTENT
        self.content = ttk.Frame(master)
        self.content.pack()

        ttk.Label(self.content, text = 'ROOT FILE PATH',font = ('sys', 10,'bold italic')).grid(row = 0, column = 0, padx = 5, sticky = 'nw')
        ttk.Label(self.content, text = 'DEST FILE PATH', font = ('sys', 10,'bold italic')).grid(row = 0, column = 1, padx = 5, sticky = 'nw')
        ttk.Label(self.content, text = 'COMMENTS', font = ('sys', 10,'bold italic')).grid(row = 3, column = 0, sticky = 'nw', padx = 100)

        #ENTRY FIELDS
        self.file_entry = ttk.Entry(self.content, width = 45, font = ('Ariel', 8))
        self.file_entry.grid(row = 1, column = 0, padx = 5)
        self.file_dest = ttk.Entry(self.content, width = 45, font = ('Ariel', 8))
        self.file_dest.grid(row = 1, column = 1, padx = 5)
        self.comments = Text(self.content, width = 50, height = 5)
        self.comments.grid(row = 4, column = 0, columnspan = 2)


        #BUTTONS
        self.browse = ttk.Button(self.content, text = 'BROWSE')
        self.browse.grid(row = 2, column = 0, sticky = 'nw', padx = 5, pady = 4)
        self.browse2 = ttk.Button(self.content, text = 'BROWSE')
        self.browse2.grid(row = 2, column = 1, sticky = 'nw', padx = 5, pady = 4)
        self.clear = ttk.Button(self.content, text = 'CLEAR')
        self.clear.grid(row = 5, column = 0, sticky = 'sw',pady = 5, padx = 5)
        self.transfer = ttk.Button(self.content, text = 'TRANSFER')
        self.transfer.grid(row = 5, column = 1, sticky = 'ne', padx = 84, pady = 5)
        self.cancel = ttk.Button(self.content, text = 'CANCEL', command = quit).grid(row = 5, column = 1, sticky = 'ne', pady = 5, padx = 5)


        #PROGRESS BAR
        value = IntVar()
        self.prog = ttk.Progressbar(self.content, orient = HORIZONTAL, length = 250, maximum = 50.0, value = 0)
        #self.prog.grid(row = 4, column = 1)


        #BIND EVENTS
        self.transfer.bind('<1>', lambda e: ctrl.transfer_(self))
        self.clear.bind('<1>', lambda e: ctrl.clear_(self))
        self.browse.bind('<1>', lambda e: ctrl.browseRoot_(self))
        self.browse2.bind('<1>', lambda e: ctrl.browseDest_(self))


    #DEFINE EVENTS
    """ def transfer_(self):
        path = self.file_entry.get()
        dest = self.file_dest.get()
        shutil.copy(path, dest)
        self.clear_()
        mb.showinfo(title='FILE TRANSFER', message='File transferred to %s' %dest)


    def browse_(self):
        dirname = fd.askopenfilename()
        self.file_entry.delete(0, 'end')
        self.file_entry.insert(0, dirname)

    def browse2_(self):
        destname = fd.askdirectory()
        self.file_dest.delete(0, 'end')
        self.file_dest.insert(0, destname)


    def clear_(self):
        self.file_entry.delete(0,'end')
        self.file_dest.delete(0,'end')
 """


def main():
    root = Tk()
    FT = FileTransfer(root)
    root.mainloop()

if __name__ == '__main__': main()