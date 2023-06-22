# https://school.programmers.co.kr/learn/courses/30/lessons/181900?language=python3
def solution(my_string, indices):
    my_string = list(my_string)
    for i in sorted(indices, reverse=True):
        del my_string[i]
    return ''.join(my_string)