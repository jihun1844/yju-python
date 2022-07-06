while True:
    print("---------------")
    print("1. 구구단 출력")
    print("2. 프로그램 종료")
    print("---------------")
    inputflow = int(input("="))
    if inputflow == 2:
        print("이용해주셔서 감사합니다")
        break
    elif inputflow <=0 or inputflow >=3:
        print("잘못 입력하셨습니다, 다시입력 하세요.")
        continue
    else:
        print("출력할 구구단의 단을 입력 하세요. 구구단의 단은 2~9 사이 입력 하세요")
        while True:
            inputnum = int(input())
            
            if inputnum <1 or inputnum >10 :
                print("2~9사이 정수를 입력해주세요")
                continue
            else :
                for num in range(1,10):
                    print(inputnum,"*",num,"=",(inputnum*num))
                break

                







