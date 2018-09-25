import datetime
import time

class OpenClosed():

    def __init__(self):

            pdx_current = datetime.datetime.now()
            pdx = pdx_current
            pdx_hour = pdx_current.hour
            pdx_minute = pdx_current.minute
            ny_hour = pdx_hour + 3
            ny = ny_hour, pdx_minute
            uk_hour = pdx_hour + 8
            uk = uk_hour, pdx_minute

            if pdx_hour >= 9 and pdx_hour <= 21:
                print(pdx)
                time.sleep(0.3)
                print('PORTLAND OFFICE // OPEN')
            else:
                print(pdx)
                time.sleep(0.3)
                print('PORTLAND OFFICE // CLOSED')

            time.sleep(0.5)
            if ny_hour >= 9 and ny <= (21, 00):
                print(ny)
                time.sleep(0.3)
                print('NEW YORK OFFICE // OPEN')
            else:
                print(ny)
                time.sleep(0.3)
                print('NEW YORK OFFICE // CLOSED')

            time.sleep(0.5)
            if uk_hour >= 9 and uk <= (21, 14):
                print(uk)
                time.sleep(0.3)
                print('LONDON OFFICE // OPEN')
            else:
                print(uk)
                time.sleep(0.3)
                print('LONDON OFFICE // CLOSED')

            print(datetime.datetime.now().time().strftime('%H:%M'))


OpenClosed()
