# https://school.programmers.co.kr/learn/courses/30/lessons/181924?language=python3
def solution(arr, queries):
    for q in queries:
        arr[q[0]], arr[q[1]] = arr[q[1]], arr[q[0]]
    return arr
