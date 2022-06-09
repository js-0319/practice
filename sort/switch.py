# 각각 N개의 자연수 원소를 갖고있는 두 개의 배열 A와 B
# 최대 K번의 바꿔치기 연산 수행 가능. 바꿔치기란 A와 B에서 각각 원소를 하나씩 골라서 서로 바꾸는 것.
# K번의 바꿔치기 안에 가능한 A의 가능한 원소의 합의 최댓값을 구하기
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # ascending
b.sort(reverse=True) # descending

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break

print(sum(a))