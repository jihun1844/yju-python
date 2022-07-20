import turtle

myturtle = turtle.Turtle()
size = 210                          #한 변의 길이
line_size = 210                     #줄긋기 할때의 줄 길이
myturtle.screen.bgcolor("gray")     #배경 색
myturtle.color("gray")              #좌표 이동할때 선이 남아서 배경과 같은 색으로 안보이게 만듬
myturtle.setposition(-200,150)      
myturtle.color("black")             #다시 컬러 블랙으로 입력

# 정사각형 3D로 만들기(마름모 3개 이어서 만들기)
myturtle.left(30)
for num in range(6):        #맨처음 육각형은 반복
    myturtle.forward(size)
    myturtle.right(60)
myturtle.right(60)
myturtle.forward(size)
myturtle.right(60)
myturtle.forward(size)
myturtle.left(120)
myturtle.forward(size)
myturtle.left(60)
myturtle.forward(size)
myturtle.left(120)
myturtle.forward(size)
myturtle.right(60)

#줄 긋기
#줄의 횟수는 마름모의 기준점의 각도가 120도, 반복할때마다 +2도 틀어지니 60회
myturtle.speed(0)                   #속도는 선 긋는게 너무 오래 걸려서 최대로 올림
for num in range(60):               #정중앙을 기준점으로 마름모 모양으로 나오게 선의 길이를 조절함 
    if num <=30:        #선의 길이   #60번 반복중에 정중간인 30을 기준으로 길이가 짧아 졌다가 원래 길이로 돌아옴
        if num >=17 and num <=30 :
            line_size += 1
            if num >25:
                line_size += 2
            if num >28:
                line_size += 1
        else:
            if num <12:
                line_size -= 2
            if 3<num<6 :
                line_size -= 3
    if num >30:
        if num >=45 and num <59 :
            line_size += 1
            if num >55:
                line_size += 2
            if num >56:
                line_size +=2
            
        else:
            if 30<num <42:
                line_size -= 2
            if 35<num<40 :
                line_size -= 1
    if num ==30 :
        myturtle.width(2)  #선명하게 보일려고 정중간 선만 굵게 그음
    #선의 각도는 한번 반복할때마다 2도 추가로 꺽고 선을 그림
    else:                           
        myturtle.width(1)
    myturtle.forward(line_size)
    myturtle.right(180)
    myturtle.forward(line_size)
    myturtle.right(180+2)

myturtle.right(180)
flow_size = 5
for flow in range(1,flow_size):
    for num in range(2):
        myturtle.right(60)
        myturtle.forward((size/flow_size)*flow)
        myturtle.right(120)
        myturtle.forward((size/flow_size)*flow) 
myturtle.left(60)

#종료
turtle.done()
