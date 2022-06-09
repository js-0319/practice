# N*M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1
# 구멍이 뚫려 있는 부분끼리 상하좌우로 붙어있는 경우 연결되었다고 가정
# 이 때 생성되는 얼음 덩어리의 숫자를 구하기
n, m = map(int, input().split())
maparr = []
for i in range(n):
  maparr.append(list(map(int, input())))

# DFS로, 현재 지점의 상하좌우를 살핀 뒤 값이 0이면서 아직 방문하지 않은 곳을 방문
def dfs(x,y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False # 예외처리
  if maparr[x][y] == 0:
    maparr[x][y] = 1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

# 물 채우기
c = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      c += 1

print(c)