# https://school.programmers.co.kr/learn/courses/30/lessons/181923?language=python3
def solution(arr, queries):
    answer = []
    for q in queries:
        tmp = 1000001
        for i in range(q[0], q[1]+1):
            if arr[i] > q[2]:
                tmp = min(tmp, arr[i])
        if tmp == 1000001:
            tmp = -1
        answer.append(tmp)
    return answer
