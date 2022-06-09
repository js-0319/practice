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