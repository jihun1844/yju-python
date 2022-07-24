import random
#랜덤값 1~20
random_list = []

plus = 0
for row in range(21):
    num = (random.randint(1,20))
    #합계 구하는 변수
    plus += num
    random_list.append(num)
print("랜덤값 : ",random_list)
#최소값
for min in random_list:
    for min_count in random_list:
        if min > min_count:
            min = min_count
print("최소값",min)
#최대값
for max in random_list:
    for max_count in random_list:
        if max < max_count:
            max = max_count
print("최대값",max)
#합계
print("합계 : ",plus)
#평균
print("평균",plus/row)

#중복값과 중복 횟수
print("중복 값   중복 회수")
count = 0
while min <21:
    for num in random_list:
        if min == num:
            count += 1
    if count >1:
        print(min,"   ",count)
    count = 0  
    min += 1
#별찍기
print("구간별 히스토그램")
plus = 0
for flow in range(4):
    for num in random_list:
        if (1+plus)< num <=(5+plus):
            count += 1
    print((1+plus),"~",(5+plus)," : ",("*"*count))
    count = 0
    plus += 5
    
    
    min += 1
    












    

    
    
    