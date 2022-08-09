stulist = []
#학생 성적 입력과 합계 평균까지의 함수
def stuavg():
    id = int(input("학번을 입력 하세요"))
    name = input("이름을 입력 하세요")
    kor = int(input("국어성적을 입력 하세요"))
    eng = int(input("영어성적을 입력 하세요"))
    math = int(input("수학성적을 입력 하세요"))
    sumavg = kor + eng + math
    avgavg = sumavg /3
    stulist.append(f"id : {id} name : {name} 국어 : {kor} 영어 : {eng} 수학 : {math} 합계 : {sumavg} 평균 : {avgavg}")
    return sumavg , avgavg
data_count = 0  
allavg = 0
allnum = 0
#전체 메뉴 반복문
while True:
    print("=============")
    print("1. 학생 성적 입력")
    print("2. 학생 목록 출력(입력순")
    print("3. 프로그램 종료")
    print("현 입력데이터 갯수 : ",data_count)
    print("전체 학생 평균 값 : ",allavg)
    print("=============")
    menu = int(input())
#1. 학생 성적 입력
    if menu == 1:
        data_count +=1
        sum , avg = stuavg()
        allnum += avg
        allavg = allnum / data_count
    if menu == 2:
        for row in range(len(stulist)):
            print(stulist[row])
    if menu == 3:
        print("프로그램 종료")
        break

        


        


#2. 학생 목록 출력 
#3. 프로그램 종료