import random

#랜덤 정답 생성 함수
def generateAnswer():
    randomNum = ""
    for _ in range(4):
        randomNum+=str(random.randint(0,9))
    return randomNum

#인풋 받는 함수
def inputNum():
    print("숫자를 입력해주세요.")
    while True:
        num = input()
        if((not num.isdigit()) or len(num) != 4):
            print("잘못된 숫자입니다. 숫자를 다시 입력해주세요.")
        else:
            break
    return num

if __name__ == '__main__':
    answer = generateAnswer()
    inNum = inputNum()
    print(inNum)

