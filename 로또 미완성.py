import random

lotto_list = []
my_lotto_list = []


while True:
    print("----------")
    print("1. 시작")
    print("2. 종료")
    print("----------")
    game_start = int(input("="))
    if game_start ==2:
        print("종료되었습니다")
        break
    if game_start <=0 or game_start >=3:
        print("다시 입력")
        continue
    else:
        for my_num in range(6):
            my_lotto = int(input("내 로또 번호를 입력하세요(6자리)"))
            if my_lotto in my_lotto_list:
                print("중복입니다, 다시 입력하세요")
                continue
            if my_lotto <=0 or my_lotto >=46:
                print("1~45 중에서 입력해주세요")
                continue
                    
            my_lotto_list.append(my_lotto)


        num = int(input("게임 수를 입력하세요"))
        for flow in range(num):
            lotto = random.sample(range(1,46),6)
            lotto_list.append(lotto)

        count = 0
        for i in my_lotto_list:  #이 리스트에 있는 수를 하나하나 반복
            if i in lotto_list:
                count += 1
        if count ==0:
            print("하나도 못맞추셨네요ㅠㅠ")
            print("로또 번호는")
            print(*lotto_list,sep='\n')
        else:
            print("총",count,"맞췄습니다")
            print("로또 번호는")
            print(*lotto_list,sep='\n')
            break
            

        




    


