# 배열의 크기 N을 첫 줄에, 각 방마다 식량의 수를 나타낸 배열을 둘쨰 줄에
# 인접한 2개의 원소를 꺼낼 수 없음
# 꺼낼 수 있는 원소의 합의 최댓값을 출력
n = int(input())
array = list(map(int, input().split()))

# i번째 원소를 더할 지 말지를 결정할 떄
# i-1번째 원소를 더했으면 i번째는 더할 수 없음
# i-2번째 원소를 더했으면 i번째를 더할 수 있음
# 따라서 a_i 는 a_i-1과 a_i-2 + i번째 원소 중 큰 것을 고르면 된다.
d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])