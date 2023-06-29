# https://school.programmers.co.kr/learn/courses/30/lessons/181936?language=python3
def solution(number, n, m):
    return 1 if not (number % n) and not (number % m) else 0
