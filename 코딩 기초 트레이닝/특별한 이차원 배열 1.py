# https://school.programmers.co.kr/learn/courses/30/lessons/181833?language=python3

def solution(n):
    answer = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    return answer