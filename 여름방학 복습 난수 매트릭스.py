import random
random_list = []
flow = 5
#랜덤값 생성
while len(random_list) <flow**2:
    num = random.randint(1,50)
    if num not in random_list:
        random_list.append(num)
        print(num," ",end="")
        if len(random_list) %flow == 0:
            print()
print("- - - - - - - - - - -")
#열의 최소 최대 중간
index = 0
max = 0
print("열")
print("최소값",end="")
for row in range(flow):
    compare = []
    mini = 100
    for col in range(flow):
        compare.append(random_list[index])
        index += 1
    
    for min in compare:
        if min < mini:
            mini = min
    print(mini," ",end="")
print()
print("최대값",end="")
index = 0
for row in range(flow):
    compare = []
    max = 0
    for col in range(flow):
        compare.append(random_list[index])
        index += 1
    
    for max_num in compare:
        if max_num > max:
            max = max_num
    print(max," ",end="")
print()
print("중간값",end="")
#리스트의 중간을 찾는 공식
if flow %2 != 0:
        num = (flow-1)/2
else:
    num = flow/2
index = 0

for row in range(flow):
    compare = []
    max = 0
    for col in range(flow):
        compare.append(random_list[index])
        index += 1
    compare.sort()    
    print(compare[int(num)],"  ",end="")
print()
print("행")
print(f"최소값   최대값    중간값")
for row in range(flow):
    compare = []
    index = row
    mini = 100
    for col in range(flow):
        compare.append(random_list[index])
        index += 5
    
    for min in compare:
        if min < mini:
            mini = min
    print(" ",mini,"       ", end="")

    for max_num in compare:
        if max_num > max:
            max = max_num
    print(max," ",end="")

    compare.sort()    
    print("    ",compare[int(num)])
#전체의 소,대,중간값
min = 100
max = 0
for value in random_list:
    if value < min:
        min = value
print("최소값",min)
for value in random_list:
    if value > max:
        max = value
print("최대값",max)

if len(random_list) %2 !=0:
    num = (len(random_list)-1)/2
random_list.sort()
print("중간값",random_list[int(num+1)])
print(random_list)

    


    

    



