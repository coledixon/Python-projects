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

            print('TIME IN PORTLAND IS: ', datetime.datetime.now().time().strftime('%H:%M'))

            if pdx_hour >= 9 and pdx_hour <= 21:
                print(pdx.strftime('%H:%M %m//%d//%Y'))
                time.sleep(0.3)
                print('PORTLAND OFFICE // OPEN')
            else:
                print(pdx)
                time.sleep(0.3)
                print('PORTLAND OFFICE // CLOSED')

            time.sleep(0.5)
            if ny_hour >= 9 and ny <= (21, 00):
                print('NEW YORK TIME: ', ny)
                time.sleep(0.3)
                print('NEW YORK OFFICE // OPEN')
            else:
                print('NEW YORK TIME: ', ny)
                time.sleep(0.3)
                print('NEW YORK OFFICE // CLOSED')

            time.sleep(0.5)
            if uk_hour >= 9 and uk <= (21, 00):
                print('LONDON TIME: ', uk)
                time.sleep(0.3)
                print('LONDON OFFICE // OPEN')
            else:
                print('LONDON TIME: ', uk)
                time.sleep(0.3)
                print('LONDON OFFICE // CLOSED')


OpenClosed()

