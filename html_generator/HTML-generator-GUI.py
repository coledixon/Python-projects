__author__ = 'ColeDixon'

import webbrowser
from tkinter import *
from tkinter import ttk


class HTMLgenerator:

    def __init__(self, master):

        #MASTER
        master.title('HTML GENERATOR')
        master.resizable(True, True)
        master.configure(background = 'black')

        #IMAGES
        img1 = PhotoImage(file = 'C:\\Users\\Dell 0381\\Desktop\\openclose.png')
        self.openclose = img1

        #HEADER
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack(fill = BOTH, expand = 1)
        self.header_frame.config
        ttk.Label(self.header_frame, image = self.openclose).grid(row = 0, column = 0)
        self.mainheader = ttk.Label(self.header_frame, text = 'Create a custom HTML website using CSS and JavaScript.\n'
                                            'Simply implement your code on the assigned page and click [RUN]. \n '
                                            'This program will build the page for you in the browser of your choice.')
        self.mainheader.grid(row = 0, column = 1)
        self.mainheader.config(background = 'white')


        #MAIN FRAME
        self.main = ttk.Frame(master)
        self.main.pack(fill = BOTH, expand = 2)


        #NOTEBOOK (TABS)
        self.notebook = ttk.Notebook(self.main)
        self.notebook.pack(fill = BOTH, expand = 1)

        #TABS
        self.prog = ttk.Frame(self.notebook)
        self.headertab = ttk.Frame(self.notebook)
        self.bodytab = ttk.Frame(self.notebook)
        self.footertab = ttk.Frame(self.notebook)
        self.csstab = ttk.Frame(self.notebook)
        self.jstab = ttk.Frame(self.notebook)
        self.notebook.add(self.prog, text = 'OVERVIEW')
        self.notebook.add(self.headertab, text = 'Header')
        self.notebook.add(self.bodytab, text = 'Body')
        self.notebook.add(self.footertab, text = 'Footer')
        self.notebook.add(self.csstab, text = 'CSS')
        self.notebook.add(self.jstab, text = 'JavaScript')

        self.headerlabel = ttk.Label(self.headertab, text = 'ENTER HEADER INFORMATION AND CSS/JavaScript LINKS:')
        self.headerlabel.pack()

        self.bodylabel = ttk.Label(self.bodytab, text = 'ENTER BODY CONTENT (use HTML tags):')
        self.bodylabel.pack()

        self.footerlabel = ttk.Label(self.footertab, text = 'ENTER FOOTER INFORMATION:')
        self.footerlabel.pack()

        self.csslabel = ttk.Label(self.csstab, text = 'ENTER CSS STYLING:')
        self.csslabel.pack()

        self.jslabel = ttk.Label(self.jstab, text = 'ENTER JavaScript AND jQuery FUNCTIONS:')
        self.jslabel.pack()

        #TEXT
        self.header = Text(self.headertab, width = 55, height = 15)
        self.header.pack()
        self.body = Text(self.bodytab, width = 55, height = 15)
        self.body.pack()
        self.footer = Text(self.footertab, width = 55, height = 15)
        self.footer.pack()
        self.css = Text(self.csstab, width = 55, height = 15)
        self.css.pack()
        self.js = Text(self.jstab, width = 55, height = 15)
        self.js.pack()


        #BUTTONS
        self.run = ttk.Button(self.main, text = 'RUN')
        self.run.pack()
        self.clear = ttk.Button(self.main, text = 'CLEAR')
        self.clear.pack()

    #EVENTS
    def clear_(self):
        self.header.delete(1.0, 'end')
        self.body.delete(1.0, 'end')
        self.footer.delete(1.0, 'end')
        self.css.delete(1.0, 'end')
        self.js.delete(1.0, 'end')


def main():
    root = Tk()
    HGen = HTMLgenerator(root)
    root.mainloop()

if __name__ == '__main__': main()
