import shutil
import os

path = 'C:\\Users\\Dell 0381\\Desktop\\A\\'
dir = os.listdir(path)
inputfile = 'C:\\Users\\Dell 0381\\Desktop\\B'
filepath = []


def filedir():

    for f in dir:
        filepath.append(f)

    for file in filepath:
        print(file)

def readfile():

    for i in filepath:
        path +i
        f = open(path +i, 'r')
        for line in f:
            print(line)

def copyfile():

    for i in filepath:
        shutil.copy(path +i, inputfile)

filedir()
readfile()
copyfile()
