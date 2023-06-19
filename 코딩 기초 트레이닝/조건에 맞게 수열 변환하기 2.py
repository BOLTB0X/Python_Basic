# https://school.programmers.co.kr/learn/courses/30/lessons/181881?language=python3
def transArr(arr):
    tmp = arr[:]
    for i in range(len(arr)):
        if not tmp[i]%2 and tmp[i] >= 50:
            tmp[i] = tmp[i] // 2
        elif tmp[i]% 2 and tmp[i] < 50:
            tmp[i] *= 2
            tmp[i] += 1
    return tmp

def solution(arr):
    answer = 0
    
    arrX = arr
    while True:
        # 먼저 문제 조건에 맞춰 배열 수정
        arrXP = transArr(arrX)

        if arrXP == arrX:
            break
        arrX = arrXP
        answer += 1
            
    return answer