import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for test_case in range(1, T + 1):
    num = input()
    # - 제외하는 함수 사용(있는지 확인)
    new_num = 0
    reverse_num = num[::-1]
    a = 0
    for i in range(len(reverse_num)):
        if (reverse_num[i] != '-'):
            new_num += int(reverse_num[i]) * 10 ** a
            a += 1
    # first_num : 맨 앞 숫자 (10 이상일 경우 16자리가 넘는다.)
    first_num = new_num // 1000000000000000

    # first_num < 10 이고, first_num == 3,4,5,6,9 이면 print(1) 아니면 print(0)
    if (first_num < 10 and 
        (first_num == 3 or first_num == 4 or
        first_num == 5 or first_num == 6 or first_num == 9)):
        print('#', test_case, ' ', 1, sep='')
    else:
        print('#', test_case, ' ', 0, sep='')