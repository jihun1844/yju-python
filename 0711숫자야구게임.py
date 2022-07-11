import random

# 랜덤값 0~9 3개 출력



count = 1
out = 0
ball_list = []
my_ball = []
while len(ball_list) <= 2:
    ball = (random.randint(0,9))
    if ball not in ball_list:
        ball_list.append(ball)
print(ball_list)

    

# 사용자 입력 값 3개(0~9까지의 정수만,중복안되게)
while True:
    ball_list_com = ball_list[:]
    print("시도횟수:",count)
    print("정수 3개를 입력하세요")
    while len(my_ball) <=2:
        mynum = int(input(":"))
        if mynum in my_ball :
            print("중복입니다, 다시입력하세요")
            continue       
        if mynum <=-1 or mynum >=10:
            print("0~9까지의 정수만 입력 하세요")
            continue  
        else:
            my_ball.append(mynum)             
    print(my_ball)
    # 사용자가 입력할때마다 ball,strike초기화
    strike = 0
    ball = 0
    
    # 자리 맞추기
    # 스트라이크는 같은 자리의 숫자가 맞으면 리스트에서 삭제하고
    # 남은 숫자로 볼 확인
    
    if ball_list[0] == my_ball[0] :
        strike +=1        
        ball_list_com.remove(ball_list[0])
    if ball_list[1] == my_ball[1] :
        strike +=1       
        ball_list_com.remove(ball_list[1])
    if ball_list[2] == my_ball[2] :
        strike +=1
        ball_list_com.remove(ball_list[2])
    
    
    

    for value in my_ball:
        if value in ball_list_com:
            ball += 1
    if ball >=1:
        print(ball, "Ball",end="") 
    if strike >= 1:
        print(" ",strike,"Strike")
    if ball == 0 and strike == 0:
        out += 1
        print("아웃",out,"번")
    count += 1
    if count <5:
        my_ball = []

    if count == 5:
        print("아까비~~졌네요..")
        print("정답은:",ball_list,"입니다")
        break
    
    if strike == 3:
        print("정답입니다!!!!!!")
        break
    continue

    
        
            

        
        
        







 


