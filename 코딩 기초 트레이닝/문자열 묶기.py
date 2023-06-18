# https://school.programmers.co.kr/learn/courses/30/lessons/181855?language=python3
def solution(strArr):
    answer = 0
    eleCnt = [0 for _ in range(31)] ## 횟수
    
    for s in strArr:
        eleCnt[len(s)] += 1
    
    for i in range(1,31):
        if eleCnt[i] == 0:
            continue
        answer = max(answer, eleCnt[i])
    return answer