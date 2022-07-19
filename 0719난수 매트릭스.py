import random

# N X N 매트릭스를 출력하라.    ok
# N 값은 키보드로부터 입력....  ok
# 좋은 프로그래머란...신속, 정확, 확장성 <-  ok

num_list = []
num_sort_list = []
num_pass = []

print("매트릭스 값 입력")
matrix = int(input())
random_num = matrix**2
# 랜덤값 1~50중에서 25개 중복없이
while len(num_list) <random_num+1:  
    num = random.randint(1,50)
    if num in num_list:
        continue
    else:            
        num_list.append(num)

#행과 열로 나눠서 죄표 넣을수 있게 만들기
for value in num_list:
    if len(num_pass) == matrix:
        num_sort_list.append(num_pass)
        print(num_pass)
        num_pass = []
    num_pass.append(value)



#열의 최소, 최대, 중간값 출력
print("열")
#앞자리수가 열이고 그 열을 하나로 모아서 비교
#num_sort_list 의 [0][0]-> [1][0].... 이렇게 행수가 올라가고 그거랑 비교
print("최소값")
for col in range(matrix):
    compare = []
    for row in range(matrix):    
        compare.append(num_sort_list[row][col])
        
    for mini in compare:
        for mini_count in compare:
            if mini > mini_count:
                mini = mini_count
    print(mini," ",end="")
print()
#최대값도 num_sort_list의 [0][0]->[1][0]...을 모아서 리스트에 넣고 최대값 비교하여 구함
print("최대값")
for col in range(matrix):
    compare = []
    for row in range(matrix):    
        compare.append(num_sort_list[row][col])
        
    for max in compare:
        for max_count in compare:
            if max < max_count:
                max = max_count
    print(max," ",end="")
print()
#중간값도 리스트에 모아서 함수sort로 정렬후 [2]를 출력
print("중간값")
for col in range(matrix):
    compare = []
    for row in range(matrix):    
        compare.append(num_sort_list[row][col])
        
    compare.sort()
    print(compare[(matrix//2)]," ",end="")
print()

#행은 이중 포문에서 row와 col의 위치를 바줘준다 이유는 열이 아니라 행을 저장해야하기때문
print("행")
print("최소값   최대값   중간값")
for row in range(matrix):                #행은 출력이 최소,최대,중간이 한줄로 출력되야 하니
    compare = []                         #첫번째 행 compare리스트가 만들어 진걸로 3개 값을 다 구함 
    for col in range(matrix):    
        compare.append(num_sort_list[row][col])

    for mini in compare:
        for mini_count in compare:
            if mini > mini_count:
                mini = mini_count
    print(" ",mini,"      ",end="")

    for max in compare:
        for max_count in compare:
            if max < max_count:
                max = max_count
    print(max,"      ",end="")
    compare.sort()
    print(compare[(matrix//2)],"      ",end="")
    print()

#전체 구하는건 구할려는 리스트가 전체리스트인 num_list로 비교
print("전체")
for mini in num_list:
    for mini_count in num_list:
        if mini > mini_count:
            mini = mini_count
print("최소값",mini)

for max in num_list:
    for max_count in num_list:
        if max < max_count:
            max = max_count
print("최소값",max)

num_list.sort()
print("중간값",num_list[(len(num_list)-1)//2])
        
