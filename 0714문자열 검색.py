
word_list = []
all_num = []

print("입력 문자열의 줄 수를 입력하세요")
line = int(input())
for value in range(1,line+1):
    count = 0
    word_ex = ""
    word_list_ex = []
    print(value,"번째 라인의 문자열을 입력하세요")
    #입력 받은 문자는 1글자씩 쪼개서 변수에 따로 넣은후 " "이 나오면 그 변수를 리스트에 저장
    word = (input())
    for value in word:
        count += 1              #count는 입력한 단어의 마지막 단어를 저장 하기위해 만듬
        if value == " " :       #" "이면 저장
            word_list_ex.append(word_ex)
            word_ex = ""  #변수 초기화

        if value != " ":            #공백이 아니면서 입력값의 마지막 글자면 리스트에 저장
            word_ex += value
            if count == len(word):
                word_list_ex.append(word_ex)
    #1라인씩 저장된 ex리스트를 다시 word리스트에 옮기고 ex리스트는 초기화 
    # 이렇게 word리스트안에 1라인을 받은 ex리스트를 넣어야 문자 찾기에서 index사용가능        
    word_list.append(word_list_ex) 
    #append가 아닌 그냥 더하기로 넣어서 전체 단어 갯수를 len으로 출력 가능 
    all_num += word_list_ex         


print(word_list)

find_count = 0
index = 0
find_index = []
print("검색할 문자열을 입력하세요")
while True:   
    find_word = input("")
    for index in range(line):
        for value in word_list[index]:          #index 0번부터 단어를 하나하나 가져옴
            if find_word == value:              #찾는 단어랑 비교
                find_count += 1
                if index+1 not in find_index:   #찾았으면 카운트 올려주고 라인 위치(index+1) 저장
                    find_index.append(index+1)
    if find_count == 0 and index == line-1:
        print("찾을수가 없습니다, 문자열을 입력하세요")
        continue
    break
print(find_word,"를 찾았습니다")
print("검색된 라인수 : ",find_index)
print("검색된 횟수 : ",find_count)
print("총 단어 수 : ",len(all_num))



# 검색 문자 문자열에서 찾기

# 프린트: 찾은 단어, 검색된 라인 수, 검색된 문자 갯수, 총단어수


