flow = 5

for num in range(flow):
    for i in range(flow - num):
        print(" ", end="")

    for k in range(num *2 +1):
        if k == 0 or k == num*2 :
            print("*" , end="")
        else :
            print(" ",end="")
    print()        


flowA = 5

for numA in range(flowA+1, 0, -1):
    for a in range(flowA-numA+1):
        print(" ",end="")

    for b in range(2*numA-1):
        if b == 0 or b == numA*2 -2 :
            print("*", end="")
        else :
            print(" ",end="")
    print()        

