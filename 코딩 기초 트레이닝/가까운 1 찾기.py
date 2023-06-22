# https://school.programmers.co.kr/learn/courses/30/lessons/181898?language=python3
def solution(arr, idx):
    for i in range(len(arr)):
        if idx <= i and arr[i]:
            return i
    return -1