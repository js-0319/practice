# 여행자 A는 1*1 격자로 나뉘어진 N*N 공간 위에 서 있다.
# 왼쪽 위 좌표를 (1,1)로 두고, A는 항상 (1,1)에서 시작한다고 가정.
# A는 한번에 상하좌우 중 골라서 이동. 입력값으로 이동 계획서를 가지고 있음.
# 공간을 벗어나는 움직임은 무시하고 최종 도착하는 좌표를 출력하기.
n = int(input())
plan = input().split()
x = 1
y = 1

for p in plan:
  if p == 'L':
    if y != 1:
      y = y - 1
  elif p == 'R':
    if y != n:
      y = y + 1
  elif p == 'U':
    if x != 1:
      x = x - 1
  elif p == 'D':
    if x != n:
      x = x + 1
  else:
    print("Wrong Input")

print(x, y)