# Quick Sort
array = list(map(int, input().split()))

def quick_sort(array, first, last):
  if first >= last:
    return
  pivot = first
  left = first + 1
  right = last
  while left <= right:
    while left <= last and array[left] <= array[pivot]:
      left += 1
    while right > first and array[right] >= array[pivot]:
      right -= 1
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]
  quick_sort(array, first, right - 1)
  quick_sort(array, right + 1, last)

quick_sort(array, 0, len(array) - 1)
print(array)