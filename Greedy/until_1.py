# 어떠한 수 N이 1이 될 때까지 시행
# N이 K로 나누어떨어지면 K로 나누거나 1을 빼는 것 중 선택
# 그 외의 경우 1을 뺌
# N과 K 입력받기
# 1까지 최소시행 횟수를 출력
n, k = map(int, input().split())

count = 0
while n > 1:
  if n % k == 0:
    n = n // k
    count += 1
  elif n < k:
    count += n - 1
    break
  else:
    t = n - ((n // k) * k)
    n -= t
    count += t

print(count)