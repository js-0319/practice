# Python Quick Sort
array = list(map(int, input().split()))

def quick_sort(array):
  if len(array) <= 1:
    return array

  pivot = array[0]
  rest = array[1:]

  left = [x for x in rest if x <= pivot]
  right = [x for x in rest if x > pivot]

  return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))