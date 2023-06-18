# https://school.programmers.co.kr/learn/courses/30/lessons/181854?language=python3
def solution(arr, n):
    if len(arr) % 2:
        for i in range(len(arr)):
            if not i % 2:
                arr[i] += n
    else:
        for i in range(len(arr)):
            if i % 2:
                arr[i] += n
    return arr