# 정수 X를 받아서, 다음과 같은 연산을 최소한으로 해 1을 만들고 연산 횟수를 출력
# 1. 5로 나누어떨어지면 5로 나누기
# 2. 3으로 나누어떨어지면 3으로 나누기
# 3. 2로 나누어떨어지면 2로 나누기
# 4. 1을 뺴기
x = int(input())

d = [0] * 30001

# Dynamic Programming(Bottom-up)
for i in range(2, x+1):
  d[i] = d[i-1]+1
  if i % 2 == 0:
    d[i] = min(d[i], d[i//2]+1)
  if i % 3 == 0:
    d[i] = min(d[i], d[i//3]+1)
  if i % 5 == 0:
    d[i] = min(d[i], d[i//5]+1)

print(d[x])
    