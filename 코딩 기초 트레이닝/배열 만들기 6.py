# https://school.programmers.co.kr/learn/courses/30/lessons/181859?language=python3
def solution(arr):
    answer = [] # 새로 만드는 배열
    i = 0
    
    while i < len(arr):
        if len(answer) == 0:
            answer.append(arr[i])
        elif len(answer) > 0 and answer[-1] == arr[i]:
            answer.pop() # 제거
        elif len(answer) > 0 and answer[-1] != arr[i]:
            answer.append(arr[i])
        i += 1
        
    if len(answer) == 0:
        return [-1]
    return answer