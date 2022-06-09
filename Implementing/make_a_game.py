# 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발
# 맵은 1*1 크기의 정사각형 격자로 이루어진 N*M 크기의 직사각형
# 각 칸은 육지 혹은 바다이고, 캐릭터는 동서남북 중 특정 방향을 바라본다
# 맵의 좌표는 (A,B)로 나타내어 A는 북쪽에서부터 떨어진 칸 수, B는 서쪽에서부터 떨어진 칸 수를 나타낸다.
# 캐릭터의 이동 방법은 다음과 같다.
# 1. 현재 위치에서 현재 방향 기준 왼쪽 방향부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터 바로 왼쪽에 가보지 않은 칸이 존재한다면, 좌회전하고 한칸 전진한다. 가보지 않은 칸이 없다면 좌회전만 하고 1번으로 돌아간다.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다일 경우에는 바라보는 방향을 유지하고 한 칸 뒤로 가고 1번으로 돌아간다. 단 뒤가 바다인 경우에는 멈춘다.
# 캐릭터가 방문한 칸의 수를 구하기
# 방향은 0 북 1 동 2 남 3 서
# 육지 여부는 0 육지 1 바다
n, m = map(int, input().split())
x, y, d = map(int, input().split())
maparr = []
for i in range(n):
  maparr.append(list(map(int, input().split())))

# v for visited
v = [[0] * m for u in range(n)]
v[x][y] = 1

# 좌회전을 정의. 1~3에서는 숫자를 1씩 줄이면 좌회전, 북쪽에서는 3이 되야 함
def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

# 각 방향 이동에 따른 효과를 list로 정리
mx = [-1, 0, 1, 0]
my = [0, 1, 0, -1]

# 캐릭터 이동 시작
visited = 1 # 첫칸 방문한상태로 시작
t = 0 # 이동하기 위해 좌회전한 횟수
while True:
  turn_left() # 1과 2에 의해 일단 좌회전을 하고 생각
  tempx = x + mx[d]
  tempy = y + my[d] # 1번에 따라 우선 가상으로 이동하고 가능한 이동인지 확인
  if v[tempx][tempy] == 0 and maparr[tempx][tempy] == 0:
    # 방문한 적이 없는 육지칸일 조건
    v[tempx][tempy] = 1 # 방문했다고 표시
    x = tempx
    y = tempy # 이동함
    visited += 1 # 하나 더 방문
    t = 0 
    continue

  else:
    t += 1 # 한번 더 돌기

  if t == 4: # 4 방향 전부 확인했으나 못 움직였을 경우
    tempx = x - mx[d]
    tempy = y - my[d] # 3번에 따라 우선 가상으로 뒤로 이동
    if maparr[tempx][tempy] == 0:
      x = tempx
      y = tempy
    else:
      break # 뒤가 바다. 3에 따라 멈춤조건임
    t = 0 

print(visited)