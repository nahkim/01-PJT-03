import sys

sys.stdin = open("_신용카드만들기1.txt")


T = int(input())
for test_case in range(1, T + 1):
    sum_ = 0
    x_ = 0
    list_ = list(map(int, input().split()))
    for i in range(len(list_)):
        if i % 2 == 0:              # 홀수자리는 2를 곱해서 더함
            x_ += list_[i] * 2      # (리스트는 0부터 시작하기 때문에 여기서 말하는 홀수자리가 짝수임)
        else:                       # 짝수자리는 그대로 더함
            sum_ += list_[i]
    less_ = (x_ + sum_) % 10        # 유효한 숫자인지 확인
    res = 10 - less_
    if less_ == 0:                  # 나머지가 0일 경우 10이나 0이 나오기 때문에 10일경우 0으로 변경
        res = 0
    print('#', test_case, ' ', res, sep='')
    