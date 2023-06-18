# https://school.programmers.co.kr/learn/courses/30/lessons/181873?language=python3
def solution(my_string, alp):
    return ''.join([i.upper() if i == alp else i for i in my_string])