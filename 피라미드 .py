flow_num = 5

for flow in range(flow_num):
    for i in range(flow_num-flow):
        print(" ",end="")
    

    for k in range(flow * 2+ 1):

        if k==0 or k== flow*2 or flow == flow_num-1 :
            print("*", end="")
        else :
            print(" ", end="")
    
    print()



