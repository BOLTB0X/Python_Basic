# https://school.programmers.co.kr/learn/courses/30/lessons/181835?language=python3

def solution(arr, k):
    answer = [a *k for a in arr] if k%2 else [a + k for a in arr]
    return answer