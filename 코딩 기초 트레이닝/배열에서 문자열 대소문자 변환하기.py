# https://school.programmers.co.kr/learn/courses/30/lessons/181875?language=python3
def solution(strArr):
    return [strArr[i].upper() if i%2 else strArr[i].lower() for i in range(len(strArr))]