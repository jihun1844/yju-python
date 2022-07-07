flow = 6
num = 5

for flowC in range(flow):
    for numC in range(flow-flowC):
        print(" ",end="")
    

    for i in range(flowC+1):
        print("*",end="")
    print()
        
for B in range(flow):
    for BB in range(B+1):
        print(" ",end="")
    
    for ii in range(num, 0, -1):
        if BB>B:
            print("*",end="")
    print()
    
    
