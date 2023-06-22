# https://school.programmers.co.kr/learn/courses/30/lessons/181894?language=python3
def solution(arr):
    if not 2 in arr:
        return [-1]
    
    firstIdx = arr.index(2)
    lastIdx = arr[::-1].index(2)
    #print(firstIdx, lastIdx)
    return arr[firstIdx:len(arr)-lastIdx]