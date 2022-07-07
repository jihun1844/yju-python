# flow = 6

# for flowC in range(flow):
#     for numC in range(flow-1):
#         if flowC >numC:
#             print("*",end="")
#     print()

# for flowB in range(flow):
#     for numB in range(flow-1,0,-1):
#         if flowB < numB-1:
#             print("*",end="")
#     print()


num = 5
median = 5//2 + 1


for row_num in range(num):   
   
    if row_num < median:
        for star_count in range(row_num + 1):
            print("*", end="")
    else:    
        for star_count in range(num - row_num):
            print("*", end="")
            
    print()