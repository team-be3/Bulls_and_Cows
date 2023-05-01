import random

#랜덤 정답 생성 함수
def generateAnswer():
    randomNum = ""
    table = ['0','1','2','3','4','5','6','7','8','9']
    random.shuffle(table)
    randomNum = "".join(table[:4])
    return randomNum

#인풋 받는 함수
def inputNum():
    print("숫자를 입력해주세요.")
    while True:
        num = input()
        if((not num.isdigit()) or len(num) != 4 or len(set(num)) != 4):
            print("잘못된 숫자입니다. 숫자를 다시 입력해주세요.")
        else:
            break
    return num

#정답 여부 판별 함수
def checkAnswer(inputNum, answer):
    strike = 0
    ball = 0
    for i in range(len(answer)):
        if inputNum[i] == answer[i]:
            strike += 1
        elif inputNum[i] in answer:
            ball += 1
    if strike == 4:
        print("정답입니다!")
    else:
        print("스트라이크: {}, 볼: {}".format(strike, ball))

if __name__ == '__main__':
    answer = generateAnswer()
    inNum = inputNum()
    print(inNum)
    while True:
        inNum = inputNum()
        checkAnswer(inNum, answer)
        if checkAnswer(inNum, answer) == "정답입니다!":
            break

