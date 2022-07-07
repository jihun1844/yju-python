flow = 5

flowA = flow-1

for num in range(flow):
    for i in range(flow-num):
        print(" ",end="")

    for kk in range((num+flowA)*2 +1):
        if kk == 0 or kk == (num+flowA)*2 :
            print("*",end="")
        elif num == 0:
            print("*",end="")
        else:
            print(" ",end="")
    print()




for numA in range(flow+1, 0, -1):
    for ii in range(flow-numA+1):
        print(" ",end="")

    for kk in range((numA+flowA)*2-1):
        if kk == 0 or kk == (numA+flowA)*2-2 or flow-flowA == numA:
            print("*",end="")
        else:
            print(" ",end="")
    print()