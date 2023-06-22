# https://school.programmers.co.kr/learn/courses/30/lessons/181899?language=python3
def solution(start, end):
    answer = []
    
    for i in range(start,-1,-1):
        if end > i:
            break
        answer.append(i)
    return answer