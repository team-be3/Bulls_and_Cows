import random

#랜덤 정답 생성 함수
def generateAnswer():
    randomNum = ""
    for _ in range(4):
        randomNum+=str(random.randint(0,9))
    return randomNum

if __name__ == '__main__':
    answer = generateAnswer()
    print(answer)

