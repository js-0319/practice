# 체스의 나이트는 8*8 격자 위에서 L자 모양으로 움직인다.
# 수직2칸 후 수평1칸 or 수직1칸 후 수평2칸
# 이 때 나이트의 위치를 입력받으면 나이트가 다음에 이동할 수 있는 경우의 수를 출력하기
# 위치는 a1 b4 와 같은 형태로 입력됨
input_pos = input()
row = int(input_pos[1])
col = int(ord(input_pos[0])) - int(ord('a')) + 1

plan = [(-2,1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

ans = 0
for p in plan:
  next_r = row + p[0]
  next_c = col + p[1]
  if next_r >= 1 and next_r <= 8 and next_c >= 1 and next_c <= 8:
    ans += 1

print(ans)