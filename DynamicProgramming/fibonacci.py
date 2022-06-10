# Fibonacci Sequence using dynamic programming

temp = [0] * 100000

def fibonacci(k):
  if k == 1 or k == 2:
    return 1
  if temp[k] != 0:
    return temp[k]
  temp[k] = fibonacci(k-1) + fibonacci(k-2)
  return temp[k]