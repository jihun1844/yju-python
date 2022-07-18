
lineNum = int(input("줄 수를 입력 하세요"))

textLine = []

# 문자열 입력, 줄 수 만큼
for index in range(lineNum):
    textLine.append(input((str(index + 1) + "번째 문장을 입력하세요")))    
    
# 검색어 입력
findWord = input("검색어를 입력 하세요")

# 검색 결과 출력
# 문자 순회
for row in range(lineNum):
    stateIndex = 0
    previousChar = ""
    nextChar = ""
    
    for col in range(len(textLine[row])):
        
        nextChar = "" if col == (len(textLine[row]) -1) else textLine[row][col + 1]
       
        print("prev : ", previousChar, " cur : ", textLine[row][col], " next : ", nextChar)
        # Matching 시작
        if stateIndex == 0 and textLine[row][col] == findWord[stateIndex]:
            stateIndex += 1
        # Matching 계속
        elif textLine[row][col] == findWord[stateIndex]:
            # 매칭 종료
            if stateIndex == (len(findWord) - 1):
                print("찾았다. ROW, COL ", row, col)
            # 매칭 계속
            else:
                stateIndex += 1              
        # 문자열이 일치하지 않을 경우 상태값 리셋
        else:
            stateIndex = 0
            
        print(textLine[row][col], " : ", end="")
        
        previousChar = textLine[row][col]