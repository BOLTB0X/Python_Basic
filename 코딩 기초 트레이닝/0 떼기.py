# https://school.programmers.co.kr/learn/courses/30/lessons/181847?language=python3
def solution(n_str):
    answer = n_str
    idx = 0
    for i in range(len(answer)):
        if answer[i] != "0":
            idx = i
            break
    return answer[i:]