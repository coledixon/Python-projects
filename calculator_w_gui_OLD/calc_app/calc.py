# base class for handling calculation logic
__author__ = 'ColeDixon'

from calc_app.app import * # application interface

class calc:

    def __init__(self, master):
       pass

    def clear_(self, app):
        app.num_entry.delete(0, 'end')

    def math_(self, app):
        pass


    def callback(self, app, number):
        app.num_entry.insert(0, number)
