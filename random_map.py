import random

map = [[" " for i in range(7)] for j in range(7)]

def map_print(): # 맵 그리기
    for i in range(7):
        print(map[i])

y = 3
x = 3
map[y][x] = "1" # 시작방

def range_out_x(x): # 리스트 범위 바깥으로 나가는 거 방지
    if x < 1:
        return x + 1
    elif x > 5:
        return x - 1
    else:
        return x
def range_out_y(y): # 리스트 범위 바깥으로 나가는 거 방지
    if y < 1:
        return y + 1
    elif y > 5:
        return y - 1
    else:
        return y

n = 1 # 일반방(시작방 포함) 개수
while n < 6: # 일반방 개수가 1일때 추가 방 생성 (일반방 개수를 최소 2로 맞추기 위한 장치)

    num = random.randint(1,100) # 확률을 표현하고 싶었음...

    if num <= 50: # 50% 확률로 y축 방향으로 연결되게 방 생성 (중복 생성 가능)
        y = random.randint(y-1,y+1)
        y = range_out_y(y)
        map[y][x] = '1'
    elif num >= 51: # 50% 확률로 x축 방향으로 연결되게 방 생성 (중복 생성 가능)
        x = random.randint(x-1,x+1)
        x = range_out_x(x)
        map[y][x] = '1'

    n = 0
    for i in range(7): # 방 개수 확인
        for j in range(7):
            if map[i][j] == '1':
                n += 1


spe_duplicity = []  # 중복 좌표 포함, 일반방과 인접해있는 빈공간 좌표들
candidate_spe = []  # 중복 좌표 제외, 일반방과 인접해있는 빈공간 좌표들

for i in range(7):
    for map_idx, room_num in enumerate(map[i]):
        if room_num == "1":
            if map[i-1][map_idx] == " ": # 위쪽 빈공간 확인
                spe_duplicity.append([map_idx, i-1])
            if map[i+1][map_idx] == " ": # 아래쪽 빈공간 확인
                spe_duplicity.append([map_idx, i+1])
            if map[i][map_idx-1] == " ": # 왼쪽 빈공간 확인
                spe_duplicity.append([map_idx-1, i])
            if map[i][map_idx+1] == " ": # 오른쪽 빈공간 확인
                spe_duplicity.append([map_idx+1, i])


for i in spe_duplicity:
    if i in candidate_spe:
        pass
    else:
        candidate_spe.append(i)

random.shuffle(candidate_spe)

confirm_spe = [] # 
for i in range(3):
    confirm_spe.append(candidate_spe[i])

for i in range(3):
    map[confirm_spe[i][1]][confirm_spe[i][0]] = str(i+2)


map_print()