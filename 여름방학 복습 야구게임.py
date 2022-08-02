import random
random_list = []
while len(random_list) < 3:         #중복X 랜덤값 3개 생성
    value = random.randint(0,9)
    if value not in random_list:
        random_list.append(value)
game_count = 1
out = 0
#게임이 끝날때 까지 찾기 반복
while game_count < 6 and out <2:
    strike = 0
    ball = 0
    my_num_list = []
    print("시도 횟수 : ",game_count)
    print("정수 3개를 입력 하세요")
    while len(my_num_list) < 3:   #중복 제외,0~9의 정수만    
        my_num = int(input(":")) 
        if my_num > 9 or my_num <0:
            print("0~9까지의 정수만 입력 하세요")
            continue
        if my_num in my_num_list:
            print("중복된 값 입니다")
        else:
            my_num_list.append(my_num)
    index = 0 
    #스트라이크랑 볼 확인
    for row in range(3):
        if random_list[index] == my_num_list[index]:
            strike += 1
        elif my_num_list[index] in random_list :
            ball +=1 
        index += 1
    if strike > 0:
        if strike == 3:
            print("정답입니다")
            break
        print(strike,"스트라이크")
    if ball > 0:
        print(ball,"볼")
    if strike == 0 and ball == 0:
        out += 1
        if out == 2:
            print("2아웃!! 게임끝")
            break
        print(f"out : {out}번")
    game_count += 1
if game_count >= 5 :
    print("게임 횟수 초과")
    print(f"정답은 : {random_list}입니다")
        


        
    

