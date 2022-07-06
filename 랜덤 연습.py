import random

lotto_num = []

while True:
    num = random.randint(1,46)
    if num not in lotto_num:
        lotto_num.append(num)

    if len(lotto_num)>5:
        print(lotto_num)
        break 

mine = []

while True:

    inputA = int(input("내 로또값 입력"))
    if inputA in mine:
        print("다시하셈")
        continue

    if inputA <=0 or inputA >45:
        print("다시 입력 해라")
        continue
    mine.append(inputA)
    if len(mine)>5:
        break

my = []
for a in lotto_num:
    if a in mine:
        my.append(a)

print("맞춘 숫자는",my,"입니다")
        
        

    

    







