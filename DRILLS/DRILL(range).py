import time

listable = [0,1,2,3]

length = len(listable)

for i in range(0,length):
    time.sleep(0.3)
    print(i)

time.sleep(0.2)
print("\n")    

mylist = [7,6,5,4,3,2,1,0]

for i in range(3,-1,-1):
    time.sleep(0.3)
    print("\t",i)

time.sleep(0.2)
print("\n")

testlist = [9,8,7,6,5,4,3,2,1]

for i in range(8,0,-2):
    time.sleep(0.3)
    print("\t\t",i)

