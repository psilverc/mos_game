--- 해야 할 일 ---
1. 시작 화면 생성
2. 맵 랜덤 생성
3. 각 방마다 지형지물과 적의 위치 설정
4. 캐릭터 움직임
5. 여러 종류의 적 생성
6. 적 움직임 및 캐릭터를 향한 유도 공격
7. 여러 종류의 아이템 및 효과 생성
8. 캐릭터 사망하면 맵과 캐릭터 상태(스텟 등) 초기화시키고 시작화면으로 돌아오기


맵 랜덤 생성 (일단 리스트로 표현해봄.)

import random

a = [[" " for i in range(7)] for i in range(7)]

def map(): # 맵 그리기
    for i in range(7):
        print(a[i])
        
y = 3
x = 3
a[y][x] = "1" # 시작방

def range_out_x(x): # 리스트 범위 바깥으로 나가는 거 방지
    if x < 0:
        return x + 1
    elif x > 6:
        return x - 1
    else:
        return x
def range_out_y(y): # 리스트 범위 바깥으로 나가는 거 방지
    if y < 0:
        return y + 1
    elif y > 6:
        return y - 1
    else:
        return y
        
n = 1 # 일반방(시작방 포함) 개수

while n < 6: # 방 개수를 6으로 맞추기 위한 장치

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
    for i in range(7): # 방 개수 확인
        for j in range(7):
            if a[i][j] == '1':
                n += 1
map()
