from tkinter import messagebox as mb
from tkinter import filedialog as fd
import shutil, os
import sqlite3 as sql
import datetime, time
# CUSTOM SCRIPTS
from MODEL import file_transfer_data as data


# BUTTON EVENTS
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

# DATA EVENTS
def inserttransaction_(self):
    path = self.file_entry.get()
    stats=[time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getmtime(path))),
            datetime.datetime.strptime(time.ctime(),'%a %b %d %H:%M:%S %Y')]
    TransID = 0
    for i in stats:
        TransID +=1
        self.c.execute("INSERT INTO Transfers VALUES(?,?,?,?)",
                    (TransID,i,i,self.comments.get(1.0,'end')))
        self.conn.commit()

def insertfile_(self):
    path = self.file_entry.get()
    newpath = self.file_dest.get()
    type = os.path.splitext(self.file_entry.get())[1]
    TransID = 0
    FileID = 0
    self.c.execute("INSERT INTO FileInfo VALUES(?,?,?,?,?)",
                (FileID, path, newpath, type, TransID))
    self.conn.commit()

def lasttransfer_(self):
    timeran = time.clock()
    print(timeran)