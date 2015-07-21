from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Feedback:

    def __init__(self, master):

        '''MASTER SETTINGS'''
        master.title('InGen INJURY REPORT SYSTEM')
        master.resizable(False, False)
        master.configure(background = 'black')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#355C7A')
        self.style.configure('TButton', background = 'white')
        self.style.configure('TLabel', background = '#355C7A')
        self.style.configure('TEntry', background = '#DFE0E1')
        self.style.configure('header.TLabel', font = ('Ariel', 18), background = 'black', foreground = '#B2B3B4')

        '''CREATE HEADER'''
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()

        self.jp = PhotoImage(file = 'C:\\Users\\Dell 0381\\Desktop\\Python practice\\Custom Projects\\icons\\apple-touch-icon-144x144.png')
        ttk.Label(self.header_frame, image = self.jp).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.header_frame, text = 'InGen Cryo-Tech // INJURY REPORT SYSTEM',
                  style = 'header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.header_frame, text = 'Thank you for visiting JURASSIC PARK. \n'
                                            'If you have accrued any injury or trauma during your visit, please \n'
                                            'leave detailed information below including DATE/TIME and SEVERITY. \n'
                                            'We hope you enjoyed your time at JURASSIC PARK. \n'
                                            'The safest, prehistoric experience on the planet').grid(row = 1, column = 1)

        '''CREATE CONTENT'''
        self.content_frame = ttk.Frame(master)
        self.content_frame.pack()

        ttk.Label(self.content_frame, text = 'NAME:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.content_frame, text = 'EMAIL:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.content_frame, text = 'INJURY REPORT:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

        '''ENTRY FIELDS'''
        self.entry_name = ttk.Entry(self.content_frame, width = 24, font = ('Ariel', 10))
        self.entry_email = ttk.Entry(self.content_frame, width = 24, font = ('Ariel', 10))
        self.text_comments = Text(self.content_frame, width = 50, height = 10, font = ('Ariel', 10))

        self.entry_name.grid(row = 1, column = 0, padx = 5)
        self.entry_email.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)
        self.text_comments.config(background = '#DFE0E1')

        '''CREATE BUTTONS'''
        self.submit = ttk.Button(self.content_frame, text = 'SUBMIT')
        self.submit.grid(row = 4, column = 0, sticky = 'e')
        self.clear = ttk.Button(self.content_frame, text = 'CLEAR')
        self.clear.grid(row = 4, column = 1, sticky = 'w')

        '''BINDING EVENT TO submit'''
        self.submit.bind('<1>', lambda e: self.submit_())
        self.clear.bind('<1>', lambda e: self.clear_())

    '''DEFINE EVENTS'''
    def submit_(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Injury Report: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear_()
        messagebox.showinfo(title = 'INJURY REPORT', message = 'REPORT SUBMITTED')


    def clear_(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')


def main():

    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == '__main__': main()