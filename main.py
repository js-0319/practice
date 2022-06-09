from collections import deque

n, m = map(int, input().split())
maze = []
for i in range(n):
  maze.append(list(map(int, input())))

mx = [-1, 1, 0, 0]
my = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x,y))
  while queue:
    x, y, = queue.popleft()
    for i in range(4):
      tempx = x + mx[i]
      tempy = y + my[i]

      if tempx < 0 or tempy < 0 or tempx >= n or tempy >= m:
        continue

      if maze[tempx][tempy] == 0:
        continue

      if maze[tempx][tempy] == 1:
        maze[tempx][tempy] = maze[x][y] + 1
        queue.append((tempx, tempy))

  return maze[n-1][m-1]

print(bfs(0,0))