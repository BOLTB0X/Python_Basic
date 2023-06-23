# https://school.programmers.co.kr/learn/courses/30/lessons/181906?language=python3
def solution(my_string, is_prefix):
    tmp = ""
    for m in my_string:
        tmp += m
        if tmp == is_prefix:
            return 1
    return 0