import sqlite3 as sql
# CUSTOM SCRIPTS
from CONTROLLER import file_transfer_controller as ctrl

#DEFINE GLOBALS
global transId
global success

# DEFINE DATABASE CONNECTION
def connectDb():
    conn = sql.connect('file_transfer.db') # db created on app load (app_main.py)
    c = conn.cursor()
   
# DATA EVENTS
""" def insertTran_(self, path, dest, os, time):
    self.inserttransaction_()
    self.insertfile_()
    shutil.copy(path, dest)
    self.clear_()
    mb.showinfo(title='FILE TRANSFER', message='File transferred to %s' %dest) """

def insertTran_(self, path, dest, os, datetime, time):
    data = [time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getmtime(path))),
            datetime.datetime.strptime(time.ctime(),'%a %b %d %H:%M:%S %Y')]
    transId = 0
    for i in stats:
        transId +=1
        try:
            c.execute("INSERT INTO Transfers VALUES(?,?,?,?)",
                    (transId, i, i, self.comments.get(1.0,'end')))
            conn.commit()
        except sqlite3.Error as e:
            self.sf.error("SQLite error encountered on INSERT execution: " + e.args[0])

def insertFile_(self):
    evalPaths_(path, dest)
    # path = self.file_entry.get()
    # dest = self.file_dest.get()
    type = os.path.splitext(self.file_entry.get())[1]
    TransID = 0
    FileID = 0
    self.c.execute("INSERT INTO FileInfo VALUES(?,?,?,?,?)",
                (FileID, path, newpath, type, TransID))
    self.conn.commit()

def lastTransfer_(self):
    timeran = time.clock()
    print(timeran)