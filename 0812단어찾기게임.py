import random
#단어의 절반을 랜덤으로 블라인드 값 정하기
#소수점은 올림하기
def blindnum(argchoice_word):    
    if len(argchoice_word) %2 != 0:
        blind_value = (len(argchoice_word)+1) /2
    else :
        blind_value = len(argchoice_word) / 2
    while len(blind_numlist)<=blind_value-1:
        value = random.randint(0,len(argchoice_word)-1)
        if value not in blind_numlist:
            blind_numlist.append(value) 
#선택 단어와 게임 카운트를 매개변수로 넣고 찾기 시작
def findword(argchoice_word,arggame_count):
    find = input()
    arggame_count += 1    
    find_count = 0    
    for row in range(len(argchoice_word)):
        if argchoice_word[row] == find and row in blind_numlist:
            blind_numlist.remove(row)            
            find_count += 1
    if find_count == 0:
        print("단어 안에 포함되어 있지 않습니다")
    if find_count !=0:
        print("입력한 알파벳 단어 내 포함 : ",find_count,"글자")    
    return arggame_count


#단어 3개 입력받고 리스트에 저장
#글자 범위는 5이상 20이하
game_count = 1
word_list = []
blind_numlist = []
while len(word_list) <3:
    word = input("입력")
    if 4< len(word) <21 :
        word_list.append(word)
    else:
        print("3이상 20이하 글자로 구성된 단어를 입력 하세요")
#글자 3개중에 랜덤으로 선택
choice = random.randint(0,2)
choice_word = word_list[choice]
print("단어 선택 완료 게임을 시작 합니다. 선택된 단어 : ",choice_word)

blindnum(choice_word)

#블라인드 해서 출력하기
while True:
    wordindex = 0
    print(game_count,"번째 시도, 아래 단어를 구성하는 알파벳 한 개 입력")
    for row in range(len(choice_word)):
        if row in blind_numlist:
            print(" _",end="")
            
        else:
            print(choice_word[wordindex],end="")
        wordindex += 1
    print()
    #단어 찾기 반복문
    ex_game_count = findword(choice_word,game_count)
    game_count = ex_game_count
    if len(blind_numlist) == 0:
        print(f"clear - 선택된 단어 : {choice_word}, 총 시도 횟수 : {game_count}")
        break
            





    


