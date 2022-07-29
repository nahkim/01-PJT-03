import sys

sys.stdin = open("_문자열의거울상.txt")

# 좌우반전을 시켜야 함
T = int(input())

for test_case in range(1, T + 1):
    words = input()
    reverse_words = words[::-1]     # 좌우 반전을 위해 문자열 뒤집음
    print('#', test_case, ' ', sep='', end='')
    # print(reverse_words)
    for word in reverse_words:      # 좌우 반전시킨 후 출력
        if word == 'b':
            print('d', end='')
        elif word == 'd':
            print('b', end='')
        elif word == 'p':
            print('q', end='')
        else:
            print('p', end='')
    print()