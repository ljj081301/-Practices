import random

def start():
    start_ques = False
    while start_ques != "y":
        start_ques = input("up&down 게임입니다.\n시작하시겠습니까? (y/n)")

        if start_ques == "y":
            com_num = int(random.randrange(1,100))

        elif start_ques == "n":
            pass
        
    return com_num

def game(end, com_num):
    usr_num = int(input("입력하세요 :"))

    if usr_num > com_num:
        print("Down!")

    elif usr_num < com_num:
        print("Up!")

    elif usr_num == com_num:
        print("맞추셨습니다!")
        end = True

    return end

while True:
    com_num = start()

    end = False

    while end != True:
        end = game(end, com_num)

