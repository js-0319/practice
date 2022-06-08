# 숫자 카드가 N*M의 형태로 놓임
# 행을 하나 고르고, 그 행에서 가장 숫자가 낮은 카드 선택
# 최대한 높은 숫자의 카드를 뽑아야 함
# 입력값은 첫 줄에 N, M 그 후 N*M으로 순서대로 숫자판 입력
# 뽑은 카드 숫자를 출력

n, m = map(int, input().split())
ans = 0

# 한줄씩 체크
for i in range(m):
  dat = list(map(int, input().split()))
  if ans < min(dat):
    ans = min(dat)

print(ans)