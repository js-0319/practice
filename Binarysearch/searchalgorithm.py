# Sequential Search
def sequential_search(n, target, array):
  for i in range(n):
    if array[i] == target:
      return i + 1

# Binary Search
# Only works if the array is sorted
# 1. Recursive Method
def binary_search(array, target, first, last):
  if first > last:
    return None
  a = (first + last) // 2 # 중간점
  if array[a] == target: # 맞춤
    return a
  elif array[a] > target: # 다운
    return binary_search(array, target, first, a - 1)
  else: # 업
    return binary_search(array, target, a + 1, last)

# 2. Iterative Method
def binary_search2(array, target, first, last):
  while first <= last:
    a = (first + last) // 2 # 중간점
    if array[a] == target: # 맞춤
      return a
    elif array[a] > target: # 다운
      last = a - 1
    else: # 업
      first = a + 1
  return None

    
  