mynum_list = []
plus = 0
print("주민번호 13자리를 입력하세요",end="")
mynum = (input())       #문자열로 사용자 주민번호 입력받음
for value in mynum:
    if value.isdigit(): # -를 제거한 사용자 주민번호를 리스트에 담음
        mynum_list.append(int(value))

check = [2,3,4,5,6,7,8,9,2,3,4,5]
# mynum_list 와 check의 각각 자릿수 끼리 곱하고 나온수를 전부 더해준다
for index in range(12):
    flow = mynum_list[index] * check[index]
    plus += flow

print(plus)
# 더한수 plus에 공식을 넣는다
value = 11 - (plus%11)
if value >=10:
    value%=10

#mynum_list의 마지막 자릿수와 같으면 일치!
if value == mynum_list[-1]:  
    print("일치합니다")
else:
    print("틀립니다")



