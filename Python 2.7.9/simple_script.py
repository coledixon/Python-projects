film = {'mariah' : ['MJC@gmail.com', 5334, 'GIRL'], 'dan' : ['dop@dop.dop', 2122, 'BOY'], 'tony' : ['tv@caregiver.net', 7901, 'BOY'], 'niki' : ['NDH@aol.com', 5412, 'GIRL'], 'misty' : ['mXs@yahoo.com', 1323, 'GIRL'], 'Kevin' : ['kevo@outlook.com', 1986, 'BROTHER']}

film = {'mariah' : ['MJC@gmail.com', 5334, 'GIRL'], 'dan' : ['dop@dop.dop', 2122, 'BOY'], 'tony' : ['tv@caregiver.net', 7901, 'BOY'], 'niki' : ['NDH@aol.com', 5412, 'GIRL'], 'misty' : ['mXs@yahoo.com', 1323, 'GIRL'], 'Kevin' : ['kevo@outlook.com', 1986, 'BROTHER']}

personsName = raw_input("Please enter a name: ").lower()

personsInfo = film[personsName]

def searchPeople(personsName):
        try:
            personsInfo = film[personsName]
            print 'Name: ' + personsName.title()
            print 'Email: ' + personsInfo[0]
            print 'Number: ' + str(personsInfo[1])
            print personsInfo[2]
        except:
            print 'NO INFORMATION FOUND'

userWantsMore = True
while userWantsMore == True:
    personsName = raw_input('Please enter a name: ').lower()
    searchPeople(personsName)
    searchAgain = raw_input('Search again? (y/n) ')
    if searchAgain == 'y':
        userWantsMore == True
    elif searchAgain == 'n':
        userWantsMore == False
        print '// GOODBYE \\'
        break
    else:
        print '// TERMINATING   SEQUENCE \\'
        print '\\  SEQUENCE TERMINATED   //'
        userWantsMore == False
        break
