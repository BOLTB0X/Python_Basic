# https://school.programmers.co.kr/learn/courses/30/lessons/181905?language=python3
def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1]+ my_string[e+1:]