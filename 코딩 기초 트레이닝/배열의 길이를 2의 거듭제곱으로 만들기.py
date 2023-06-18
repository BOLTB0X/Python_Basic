# https://school.programmers.co.kr/learn/courses/30/lessons/181857?language=python3import math

# 거듭제곱 판단
def isPowerTwo(n):
    return n > 0 and (n & (n-1)) == 0

def solution(arr):
    
    while not isPowerTwo(len(arr)):
        arr.append(0)
        
    return arr