import random

a = [[" " for i in range(5)] for i in range(5)]

def map(): # 맵 그리기
    for i in range(5):
        print(a[i])

y = 2
x = 2
a[y][x] = "1" # 시작방

def range_out_x(x): # 리스트 범위 바깥으로 나가는 거 방지
    if x < 0:
        return x + 1
    elif x > 4:
        return x - 1
    else:
        return x
def range_out_y(y): # 리스트 범위 바깥으로 나가는 거 방지
    if y < 0:
        return y + 1
    elif y > 4:
        return y - 1
    else:
        return y

n = 1 # 일반방(시작방 포함) 개수
while n==1: # 일반방 개수가 1일때 추가 방 생성 (일반방 개수를 최소 2로 맞추기 위한 장치)

    for i in range(5): # 방 5개 생성 (중복 생성 가능)
        num = random.randint(1,100) # 확률을 표현하고 싶었음...

        if num <= 50: # 50% 확률로 y축 방향으로 연결되게 방 생성 (중복 생성 가능)
            y = random.randint(y-1,y+1)
            y = range_out_y(y)
            a[y][x] = '1'
        elif num >= 51: # 50% 확률로 x축 방향으로 연결되게 방 생성 (중복 생성 가능)
            x = random.randint(x-1,x+1)
            x = range_out_x(x)
            a[y][x] = '1'

    n = 0
    for i in range(5): # 방 개수 확인
        for j in range(5):
            if a[i][j] == '1':
                n += 1
    print(n)

map()

