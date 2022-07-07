import random

random_list = []
while len(random_list)<21:
    num = random.randint(1,20)
    random_list.append(num)

print("랜덤 값:")   
flow_count = 0
for flow in random_list:
    print(" ",flow,end="")
    flow_count+=1
    if flow_count ==10:
        print()
print()


for miniC in random_list:
    for mini in random_list:
        if miniC > mini:
            miniC = mini
print("최소값  :",miniC)

for maxC in random_list:
    for max in random_list:
        if maxC < max:
            maxC = max
print("최대 값 :",maxC)

plusnum = 0
for plus in random_list:
    plusnum += plus
print("합계    :",plusnum)

print("평균    :",plusnum/20)

print("중복 값   중복 회수")



same_list = []
count = 0
while miniC <20:
    for sameC in random_list:
        if miniC == sameC:
            same_list.append(sameC)
            count += 1
    if count >1 and same_list[0] <10:
        print("  ",same_list[0],"       ",count)
    if count >1 and same_list[0] >=10:
        print("  ",same_list[0],"      ",count)
    count = 0
    same_list = []
    miniC += 1

print("구간별 히스토그램")

star_list = []
mininum = 1
maxnum = 5
for i in range(4):
    for starC in random_list:
        if starC >=mininum and starC <=maxnum :
            star_list.append(starC)
    print(mininum,"~",maxnum,":",("*"*len(star_list)))
    star_list = []
    mininum += 5
    maxnum += 5




            

# 최소값부터 하나하나 비교 해서 중복값 리무브로 없애기

            
    
        



    
    

    