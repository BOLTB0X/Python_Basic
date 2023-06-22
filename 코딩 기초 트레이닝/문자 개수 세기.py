# https://school.programmers.co.kr/learn/courses/30/lessons/181902?language=python3
def solution(my_string):
    answer=[0]*52
    
    for s in my_string:
        if s.isupper():
            answer[ord(s)-65] += 1
        else:
            answer[ord(s)-71] += 1
    return answer