#프로그램 실행 메뉴 
data_count = 0
allstulist = []
allstuAvg = 0
def menu1():
        Studentlist = []
        StudentID = int(input("학번을 입력 하세요"))
        name = input("이름을 입력 하세요")
        korean = int(input("국어 성적을 입력 하세요"))
        english = int(input("영어 성적을 입력 하세요"))
        math = int(input("수학 성적을 입력 하세요"))
        Average = (korean + english + math)/3
        Studentlist.append("ID"+str(StudentID)+"   name : "+str(name)+"   korean : "+str(korean)+"   english : "+str(english)+"   math : "+str(math)+"   Average : "+str(Average))
        return Studentlist,Average
while True:
    menu = 0
    print("=========================")
    print("1. 학생 성적 입력")
    print("2. 학생 목록 출력(입력순)")
    print("프로그램 종료")
    print("현 입력 데이터 갯수 : ",data_count)
    print("전체 학생 평균 값 :",allstuAvg)
    print("=========================")
    menu = int(input())
    #1번 학생 성적 입력
    
    if menu == 1:
        data_count += 1
        stulist , stuAvg = menu1()
    allstulist.append(stulist)
    allstuAvg += stuAvg
    allstuAvg /= data_count
    #2번 학생목록 출력@함수
    if menu == 2:
        for row in range(len(allstulist)):
            print(allstulist[row])
    if menu == 3:
        break
    





#3프로그램 종료