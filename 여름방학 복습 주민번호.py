value = (input("주민번호를 입력하세요"))
#체크 하는 수
check_index = 2
allnum = 0
index = 0
#입력한 주민번호 체크 인덱스랑 곱하기
for row in range(len(value)):
    if index == 13:
        break
    print(value[index])
    if value[index].isdigit():        
        num = (int(value[index])) * check_index
        allnum += num
        if check_index == 9:
            check_index=1
        check_index+=1
    index += 1
print(allnum)
#유효한지 검사하는 공식
flow= 11 - (allnum % 11) 
if flow >=10:
    flow %= 10
#맨 뒷자리랑 비교
print(value[13])
if flow == int(value[13]):
    print("유효합니다")
else:
    print("틀립니다")
