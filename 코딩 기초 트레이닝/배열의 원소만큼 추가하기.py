# https://school.programmers.co.kr/learn/courses/30/lessons/181861?language=python3
def solution(arr):
    answer = []
    
    for a in arr:
        for _ in range(a):
            answer.append(a)
    return answer