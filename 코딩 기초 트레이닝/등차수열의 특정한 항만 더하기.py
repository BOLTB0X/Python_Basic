# https://school.programmers.co.kr/learn/courses/30/lessons/181931?language=python3
def solution(a, d, included):
    answer = 0

    for i in range(len(included)):
        if included[i]:
            answer += a
        a += d
    return answer
