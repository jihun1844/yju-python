import random
my_random_list = []
lotto_list = []
mini_list = []
while True:
    print("---------")
    print("1.수동")
    print("2.자동")
    print("---------")
    menu = (int(input("=")))
    if menu <= 0 or menu >= 3 :
        print("다시 입력 하세요")
        continue
    if menu == 2:
        while len(my_random_list) <6:
            my_random2 = random.randint(1,46)
            if my_random2 in my_random_list:
                continue
            my_random_list.append(my_random2)
        
        for mini_count in my_random_list:
            for mini in my_random_list:
                if mini_count > mini:
                    mini_count = mini


        while mini_count <=45 :
            for num in my_random_list:
                if num == mini_count:
                    mini_list.append(num)
                    mini_count += 1
            mini_count += 1
        print("내 로또값")
        print(mini_list)
        mini_list = []
          

    else:
        while len(my_random_list) <6:
            my_random1 = int(input("1에서 45까지의 정수를 입력하세요:"))
            if my_random1 in my_random_list:
                print("중복입니다. 다시 입력하세요")
                continue
            if my_random1 <=0 or my_random1 >=46:
                print("1~45사이의 정수만 입력 하세요")
                continue
            my_random_list.append(my_random1)
        
        for mini_count in my_random_list:
            for mini in my_random_list:
                if mini_count > mini:
                    mini_count = mini


        while mini_count <=45 :
            for num in my_random_list:
                if num == mini_count:
                    mini_list.append(num)
                    mini_count += 1
            mini_count += 1
        print("내 로또값")
        print(mini_list)
        mini_list = []

    while len(lotto_list) <6:
        lotto = random.randint(1,46)
        if lotto not in lotto_list:
            lotto_list.append(lotto)
        else:
            continue

    for mini_count in lotto_list:
            for mini in lotto_list:
                if mini_count > mini:
                    mini_count = mini

    while mini_count <=45 :
        for num in lotto_list:
            if num == mini_count:
                mini_list.append(num)
                mini_count += 1
        mini_count += 1
    
    

    
    while True:
        plus_num = random.randint(1,46)
        if plus_num in lotto_list:
            continue
        else:
            break

    print("이번주 로또 값")
    print(mini_list,"보너스",plus_num)
    

    count = 0
    plus = 0
    
    for mynum in my_random_list:
        for num in lotto_list:
            if mynum == num:
                count += 1
        if plus_num in my_random_list:
                plus +=1
    if count == 6:
        print("전부 다 맞았습니다. 1등입니다!!")
    if count == 5 and plus == 0:
        print(count,"개 맞았습니다. 3등입니다")
    if count == 5 and plus == 1:
        print("보너스 포함 6개 맞았습니다. 2등입니다")
    if count <5 :
        print("아쉽네요",count,"개 맞았습니다.")
    my_random_list = []
    lotto_list = []
    break
        
        




    
    
    
    
        



    