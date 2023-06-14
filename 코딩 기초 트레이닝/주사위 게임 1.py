# https://school.programmers.co.kr/learn/courses/30/lessons/181839?language=python3
def solution(a, b):
    if a%2 and b%2:
        return a*a + b*b
    elif a%2 or b%2:
        return 2*(a+b)
    elif not a%2 and not b%2:
        return abs(a-b)