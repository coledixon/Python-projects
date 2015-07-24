__author__ = 'ColeDixon'
import time
import datetime as dt
students = int(input('NUMBER OF ACTIVE STUDENTS: '))
twenty = int(input('NUMBER OF STUDENTS STUDYING <= 20hrs/week: '))
thirty = int(input('NUMBER OF STUDENTS STUDYING 30hrs/week: '))
forty = int(input('NUMBER OF STUDENTS STUDYING >= 40hrs/week: '))

def math():
    t = dt.datetime.now()
    today = t.strftime('%m/%d/%Y')
    twen = twenty * 20
    thr = thirty * 30
    fort = forty * 40

    if (twenty+thirty+forty) > students:
        print('ERROR: NUMBER OF STUDYING STUDENTS CANNOT BE GREATER THAN NUMBER OF STUDENTS ENROLLED')
        exit()
    if (twenty+thirty+forty) != students:
        print(students - (twenty+thirty+forty), 'UNACCOUNTED FOR ACTIVE STUDENTS.')

    time.sleep(0.5)
    print('For the week ending on ' +today, 'students studied', (twen+thr+fort), 'hours')


math()





