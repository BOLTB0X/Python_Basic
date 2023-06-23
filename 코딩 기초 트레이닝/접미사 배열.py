# https://school.programmers.co.kr/learn/courses/30/lessons/181909?language=python3
def solution(my_string):
    return sorted([my_string[i:len(my_string)] for i in range(len(my_string))])