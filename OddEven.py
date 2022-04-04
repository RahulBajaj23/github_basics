list1 = []
countEven = 0
countOdd = 0
num = int(input("Enter No. of Elements : "))
for i in range(num):
    list1.append(int(input("Enter Ele : ")))
    
for i in list1:
    if i % 2 == 0:
        ksdjfhksjdfhj
        countEven += 1
    elif i % 2 != 0:
        countOdd += 1
    else:
        print("Invalid No.")

print("Odd Count : {}, Even Count : {}".format(countOdd, countEven))
