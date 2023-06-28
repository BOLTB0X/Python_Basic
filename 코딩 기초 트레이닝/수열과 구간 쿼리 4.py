# https://school.programmers.co.kr/learn/courses/30/lessons/181922
def solution(arr, queries):
    answer = arr

    for q in queries:
        for i in range(q[0], q[1]+1):
            if i % q[2] == 0:
                answer[i] += 1
    return answer
