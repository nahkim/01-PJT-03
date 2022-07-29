import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    list_ = list(map(int, input().split()))
    average = sum(list_) / N    # 평균
    count = 0
    for person in list_:        # 평균 이하인 사람의 수를 구함
        if average >= person:
            count += 1
    print('#', test_case, ' ', count, sep='')