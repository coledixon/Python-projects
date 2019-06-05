from tkinter import messagebox as mb
from tkinter import filedialog as fd

#DEFINE EVENTS
def transfer_(self):
    path = self.file_entry.get()
    dest = self.file_dest.get()
    shutil.copy(path, dest)
    self.clear_()
    mb.showinfo(title='FILE TRANSFER', message='File transferred to %s' %dest)


def browseRoot_(self):
    dirname = fd.askopenfilename()
    self.file_entry.delete(0, 'end')
    self.file_entry.insert(0, dirname)

def browseDest_(self):
    destname = fd.askdirectory()
    self.file_dest.delete(0, 'end')
    self.file_dest.insert(0, destname)


def clear_(self):
    self.file_entry.delete(0,'end')
    self.file_dest.delete(0,'end')
