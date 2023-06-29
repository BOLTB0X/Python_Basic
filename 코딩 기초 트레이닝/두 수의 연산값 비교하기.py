# https://school.programmers.co.kr/learn/courses/30/lessons/181938?language=python3
def solution(a, b):
    return 2*a*b if 2*a*b > int(str(a)+str(b)) else int(str(a)+str(b))
