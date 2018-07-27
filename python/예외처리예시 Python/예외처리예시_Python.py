def IncreaseNumber(n):
    if (n < 0):
        print("양의 정수를 입력해주세요.")
    elif (n == 0):
        print("0은 입력할 수 없습니다.")
    return n+1

def main():

    print("양의 정수를 입력해주세요.")

    while True:

        num = int(input(":"))
        if num > 0:
            print("입력한 정수에서 1을 증가시킨 값 : %s"%IncreaseNumber(num))
       
        elif num == 0 :
            print("0은 입력할 수 없습니다. 양의 정수를 다시 입력해주세요.")
            continue

        elif num < 0:
            print("%s은 양의 정수가 아닙니다. 양의 정수를 다시 입력해주세요."%num)
            continue

        break

main()

