# N을 입력받고, 0시 0분 0초부터 N시 59분 59초까지 모든 시각 중
# 3이 하나라도 포함되는 경우의 수 출력
n = int(input())
ans = 0

for i in range(n+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        ans += 1

print(ans)