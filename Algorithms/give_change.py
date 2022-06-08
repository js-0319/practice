# 거스름돈
# 500원, 100원, 50원, 10원 동전이 있다.
# 손님에게 줘야 할 돈을 최소한의 동전으로 지급하기
# 최소 동전의 수 출력

n = int(input())
count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
  count += n // coin
  n %= coin

print(count)