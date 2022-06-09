# Selection Sort
array = list(map(int, input().split()))

for k in range(len(array)):
  minidx = k
  for l in range(k+1, len(array)):
    if array[minidx] > array[l]:
      minidx = l
  array[k], array[minidx] = array[minidx], array[k] # Swap

print(array)
      
      