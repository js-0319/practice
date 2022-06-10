# 전자 매장에 각각 정수 형태의 고유 번호를 가진 N개의 부품
# M개의 부품을 의뢰받았을 때 해당 부품이 있는지 하나씩 확인하기
# 입력은 첫 줄에 N, 둘째 줄에 부품 리스트, 셋째 줄에 M, 넷째 줄에 의뢰 리스트
# 출력은 의뢰 리스트 앞에서부터 확인해서 no yes yes 와 같은 형식으로 출력
def binary_search(array, target, first, last):
  while first <= last:
    a = (first + last) // 2
    if array[a] == target:
      return a
    elif array[a] > target:
      last = a - 1
    else:
      first = a + 1
  return None

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
request = list(map(int, input().split()))

for r in request:
  res = binary_search(array, r, 0, n - 1)
  if res == None:
    print('no' + ' ')
  else:
    print('yes' + ' ')