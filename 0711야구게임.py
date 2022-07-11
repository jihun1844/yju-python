# 0~9까지 랜덤값생성(중복X)
import random
random_ball = []

count = 1
while len(random_ball) < 3:
    value = random.randint(0,9)
    if value not in random_ball:
        random_ball.append(value)

print("정답",random_ball)


# 사용자 입력값 0~9까지 (중복X)
# strike, ball을 while안에 선언해서 반복될때마다 초기화
while count <5:
    strike = 0
    ball = 0
    my_ball = []
    print("시도횟수:",count)
    print("정수 3개를 입력하세요")
    while len(my_ball) < 3:
        value = int(input(":"))
        if value in my_ball:
            print("중복입니다. 다시 입력하세요")
            continue
        if value < 0 or value > 9:
            print("0~9사이의 정수만 입력하세요")
            continue
        my_ball.append(value)
    my_random_com = my_ball[:]

    # 각각 리스트에서 같은자리의 숫자가 같으면 strike+
    # 그리고 복사한 리스트에서 strike맞은 숫자를 삭제

    if random_ball[0] == my_ball[0]:
        strike += 1
        #my_random_com에서 random_ball의 0번째 자리의 숫자를 삭제
        my_random_com.remove(random_ball[0]) 
        
    if random_ball[1] == my_ball[1]:
        strike += 1
        my_random_com.remove(random_ball[1]) 
        
    if random_ball[2] == my_ball[2]:
        strike += 1
        my_random_com.remove(random_ball[2])

    if strike >=1 :
        print(strike,"strike")   
    
    if strike == 3:
        print("축하합니다. 정답!")
        break

    # strike이 삭제된 my_random_com와 random_ball을 비교 해서 ball찾기
    # 그래야 strike맞은 숫자가 ball에서 중복으로 숫자가 안올라감
    for value in my_random_com:
        if value in random_ball:
            ball += 1
    if ball >=1:
        print(ball,"Ball")
    if strike == 0 and ball == 0:
        print("아웃!!")
    count += 1
    if count == 5:
        print("게임횟수 초과!")
        print("정답은",random_ball,"입니다")
    


    

        





