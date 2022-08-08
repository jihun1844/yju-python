#사용자 입력값 5개 받고 리스트에 넣기


def input_value(flow):
    mylist = []    
    for row in range(flow):
        print(row+1,end="")
        value = input(str("번째 정수 입력"))
        mylist.append(value)


input_value(int(input("정수 갯수")))
#리스트에 있는 수를 오름차순을 정렬
#리스트 수를 비교하며 제일 큰 수를 제일 뒤로 보내기를 반복
def mysort(arg_mylist):
    sortlist = []
    while len(arg_mylist) != 0:
        for num in arg_mylist:
            if value < num:
                value = num
        sortlist.append(value)
        arg_mylist.remove(value)
        value = str(1)
print(sortlist)






