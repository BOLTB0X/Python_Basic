# https://school.programmers.co.kr/learn/courses/30/lessons/181942?language=python3
def solution(str1, str2):
    return "".join((str1[i]+str2[i]) for i in range(len(str1)))
