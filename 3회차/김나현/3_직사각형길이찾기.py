import sys

sys.stdin = open("_직사각형길이찾기.txt")

# 직사각형의 세 변의 길이가 주어지고 나머지 변의 길이를 구해야하기 때문에
# 길이는 2개가 동일하기 때문에 동일하지 않은 변의 길이가 정답이 된다.
T = int(input())

for test_case in range(1, T + 1):
    dict_ = {}
    list_ = list(map(int, input().split()))
    for ele in list_:   # 주어진 세 변의 길이로 dict_에 갯수를 넣음
        if ele in dict_:
            dict_[ele] += 1
        else:
            dict_[ele] = 1
    for k, v in dict_.items():
        # print(k , v)
        # 직사각형의 경우 구하고자하는 변의 길이가 1개인 key가 정답
        # 정사각형의 경우 dict_의 value가 3이기 때문에 나머지로 확인해야함
        if v % 2 == 1:
            print('#', test_case, ' ', k, sep='')
            break