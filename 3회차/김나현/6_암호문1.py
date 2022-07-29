import sys

sys.stdin = open("_암호문1.txt")

for i in range(1, 11):
    dict_ = {}  # dict 말고 튜플이나 다른 자료형 찾아보기
    first = int(input())
    second = list(map(int, input().split()))    # 다른 방법도 찾아보기 튜플로
    for j in range(first):
        dict_[second[j]] = j + 1
    third = int(input())
    # forth를 어떻게 정제할지 생각하기 -> 2차원 배열(I, x, y, s)
    # python 연결리스트 있는지 확인해보기
    # 튜플 확인
    forth = list(map(int, input().split()))
    # print(forth)
    num = 0
    for _ in range(third):
        x = forth[num + 1]  # 1
        y = forth[num + 2]  # 5
        s = num + 3         # 8
        # dict_의 value가 x인 값을 찾고, x보다 큰 모든 value값 + y 해주기 (for)
        # dict_의 value가 x + 1부터 값넣기 (for문으로 y번 돌리기)





        num += y + 3
    # res에 forth를 value순서대로 출력
    # print('#', i, ' ', res, sep='')