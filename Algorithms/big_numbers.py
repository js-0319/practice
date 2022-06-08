# 배열의 크기 N, 더할 횟수 M, 중복해서 연속 사용 제한 K
# 크기가 N인 배열에 있는 수에서 뽑아서 M번 더한 값을 구하는데, 하나의 숫자를 K번 초과해서 더할 수 없음.
# 그렇게 구할 수 있는 최댓값을 구하기

# 입력값 받기
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

max = data[n-1]
second = data[n-2]

# 최댓값k번과 두번째값1번을 묶어서 k+1 크기의 반복행이 있음
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * max
result += (m - count) * second
# M의 크기가 매우 커지면 for문 사용시 시간초과할 수 있으니 for 문 없이 정리

print(result)

  