# https://school.programmers.co.kr/learn/courses/30/lessons/181883?language=python3
def solution(arr, queries):
    answer = arr
    
    for q in queries:
        for i in range(q[0],q[1]+1):
            answer[i] += 1
    return answer