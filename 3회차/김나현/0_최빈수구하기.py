import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())

for _ in range(T):
    test_case = int(input())    # 테스트 케이스 입력 받기
    student_dict = {}           # 딕셔너리에 점수 넣기 위해 생성
    student_list = list(map(int, input().split()))  # 1000명의 수학성적을 list에 넣음
    for student in student_list:    # 1000명의 학생들을 확인
        if student in student_dict: # student_dict에 학생들의 점수가 존재한다면
            student_dict[student] += 1  # student_dict에 +1
        else:
            student_dict[student] = 1   # 없다면 student_dict에 1
    max_value = max(student_dict.values())  # 가장 많은 value 값 찾음
    res = []
    for k, v in student_dict.items():   # student_dict을 확인하는데
        if v == max_value:              # 가장 큰 value값이라면
            res.append(k)               # res 리스트에 삽입
    max_key = max(res)                  # 리스트 안에서 가장 큰 key값 찾기
    print('#', test_case, ' ', res[0], sep='')  # 출력