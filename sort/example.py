# 첫 줄에 수열의 개수 입력
# 둘째 줄부터 순차적으로 수열 입력
# 내림차순으로 정렬
n = int(input())
array = []
for i in range(n):
  array.append(int(input()))

def quick_sort(array):
  if len(array) <= 1:
    return array
  pivot = array[0]
  rest = array[1:]

  left = [x for x in rest if x > pivot]
  right = [x for x in rest if x <= pivot]

  return quick_sort(left) + [pivot] + quick_sort(right)

array = quick_sort(array)
print(array)