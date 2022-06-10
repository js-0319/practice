# 길이가 일정하지 않은 떡볶이 떡. 다만 한 봉지 안의 총량은 일정
# 일렬로 다양한 길이의 떡을 늘어놓고 절단기로 높이 H를 지정
# 손님은 H로 자르고 난 나머지 길이를 가져갈 수 있음
# 손님이 M 이상의 떡을 가져가기 위한 절단기 높이 H의 가능한 최댓값
n, m = map(int, input().split())
array = list(map(int, input().split()))

first = 0
last = max(array)
ans = 0
while first <= last:
  d = 0
  a = (first + last) // 2
  for length in array:
    if length > a:
      d += length - a
  if d < m:
    last = a - 1
  else:
    ans = a
    first = a + 1

print(ans)

  