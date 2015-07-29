__author__ = 'ColeDixon'
import time
import datetime as dt
import random

class StudentHours:

    def __init__(self):
        self.t = dt.datetime.now()
        self.today = self.t.strftime('%m/%d/%Y')
        self.students = int(input('NUMBER OF ACTIVE STUDENTS: '))
        self.twenty = int(input('NUMBER OF STUDENTS STUDYING <= 20hrs/week: '))
        self.thirty = int(input('NUMBER OF STUDENTS STUDYING 30hrs/week: '))
        self.forty = int(input('NUMBER OF STUDENTS STUDYING >= 40hrs/week: '))
        self.courses = int(input('NUMBER OF COURSES COMPLETED: '))
        self.twen = self.twenty * random.randrange(5,20,1)
        self.thr = self.thirty * 30
        self.fort = self.forty * 40
        self.count = self.twenty+self.thirty+self.forty
        self.hours = self.twen+self.thr+self.fort
        self.comps = self.count / self.courses

        self.study_hours()
        self.avg_days()

    def study_hours(self):

        if self.count > self.students:
            print('ERROR: NUMBER OF STUDYING STUDENTS CANNOT BE GREATER THAN NUMBER OF ACTIVE STUDENTS')
            print('TRY AGAIN. WITHOUT CHEATING!')
            self.__init__()

        if self.count != self.students:
            print(self.students - self.count, 'UNACCOUNTED FOR ACTIVE STUDENTS.')

        time.sleep(0.5)
        print('For the week ending on ' +self.today, 'students studied', self.hours, 'hours')

    def avg_days(self):

        print('Students averaged about %i' %self.comps, 'days per course.')

def main():
    StudentHours()

if __name__  == '__main__': main()






