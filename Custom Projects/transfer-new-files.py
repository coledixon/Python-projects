import shutil
import os
import datetime as dt
import time

path = 'C:\\Users\\Dell 0381\\Desktop\\A\\'
dir = os.listdir(path)
inputfile = 'C:\\Users\\Dell 0381\\Desktop\\B'
filepath = []

def transferfile():
    trans = 0
    for f in dir:
        filepath.append(f)

    for file in filepath:
        print(file)

    t = dt.datetime.strptime(time.ctime(),'%a %b %d %H:%M:%S %Y')
    curday = t.strftime('%Y-%m-%d')
    for f in filepath:
        mod = time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime(path +f)))
        if mod == curday:
            trans +=1
            shutil.copy(path +f, inputfile)

    print('%i files transferred.' %trans)

transferfile()