line =int(input("문자열의 줄수를 입력하세요"))

textlist = []
find_count = 0
flowline = []
text_list_ex = []
word_ex = ""
previousword = ""
nextword = ""
for flow in range(line):
    text = (input(str(flow+1) + "번째 문장을 입력"))
    textlist.append(text)
    text_count = 0
    for value in text:
        text_count += 1                              #count는 입력한 단어의 마지막 단어를 저장 하기위해 만듬
        if value != " ":                        #입력받는 valur가 공백이아니라 문자일때 임시 변수에 문자 하나씩 추가
            word_ex += value
            if text_count == len(text):              #마지막 글자는 뒤에 공백이 없을때 그냥 바로 리스트에 단어 추가
                text_list_ex.append(word_ex)
                word_ex = ""

        if value == " " :                       #공백일때 저장
            if word_ex != "" :                  #하지만 입력값에 공백만 여러번 나오는 경우엔 임시로 스펠링을 받는 변수가( )이면 작동 안함
                text_list_ex.append(word_ex)
                word_ex = "" 

print("검색할 문자열을 입력하세요")
#검색 결과 출력
#문자 순회
while True:
    findword = input()
    for row in range(len(textlist)):
        index = 0
        for col in range(len(textlist[row])):   
            if col == len(textlist[row])-1:
                nextword = ""
            else:
                nextword = textlist[row][col+1]
            #검색 시작
            if index == 0 and textlist[row][col] == findword[index]:
                if not previousword.isalpha():
                    if len(findword) != 1:         
                        index += 1
            
            elif textlist[row][col] == findword[index]:
                #검색 종료
                if index == (len(findword)-1) and not nextword.isalpha():
                    find_count += 1
                    if row not in flowline:
                        flowline.append(row)
                    
                    index = 0
                #검색 계속
                else:
                    if len(findword) != 1:
                        index +=1
                    if index ==len(findword):
                        index = 0
            #문자열이 틀리면 index 리셋
            else :
                index = 0
            previousword = textlist[row][col]
    if find_count == 0 :
        print("찾을수가 없습니다, 검색할 문자열을 입력하세요")
        continue
    break
print("검색된 라인 수 : ",flowline)
print("검색된 횟수",find_count)
print("총 단어 수",len(text_list_ex))






        

     
        

