my_list = []
my_list_ex = []
value_ex = ""
line=int(input("줄수 입력"))
#입력한 줄 수만큼 문자열 입력 받기
for row in range(line):   
    text_count = 0
    print((row+1),"번째 라인의 문자열을 입력하세요")
    value = input()
    #총 단어수를 찾기위해 공백을 빼고 단어만 ex리스트에 넣기
    for row in value:
        text_count += 1
        if row == " " or text_count == len(value):
            if value_ex != "":
                my_list_ex.append(value_ex)
                value_ex = ""
        if row != " ":
            value_ex += row
    my_list.append(value)
while True:
    find = input("검색할 문자열을 입력하세요")
    #검색 문자열과 리스트에 있는 문자열을 비교
    #비교할때 앞글자랑 뒷글자 확인
    index = 0
    count = 0
    nextword = ""
    line_find = []
    for row in range(line):
        previousword = " "
        for col in range(len(my_list[row])):
            print(my_list[row][col])
            if col +1 == len(my_list[row]):
                nextword = " "
            else :
                nextword = my_list[row][col+1]
            #검색 시작
            if my_list[row][col] == find[index] and previousword == " " and index == 0:
                index += 1
            elif my_list[row][col] == find[index] and index != 0:
                    index += 1
                #검색 종료
                    if index == (len(find)):
                        index = 0
                        if  nextword == " ":
                            count += 1
                            if (row+1) not in line_find:
                                line_find.append(row+1)
            else:
                index = 0
            previousword = my_list[row][col]
    #검색된 문자가 없을때
    if count == 0:
        print("찾을수가 없습니다")
    else :
        print(find,"를 찾았습니다")
        break
print("검색된 라인수 : ",line_find)
print("검색된 횟수 : ",count)
print("총 단어 수 : ",len(my_list_ex))


