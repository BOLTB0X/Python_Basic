# https://school.programmers.co.kr/learn/courses/30/lessons/181830?language=python3
def solution(arr):
    answer = []
    
    maxLen = max(len(arr), len(arr[0]))
    
    for i in range(maxLen):
        tmp = []
        for j in range(maxLen):
            # 길이를 추월했을 떄 
            if i >= len(arr) or j >= len(arr[0]):
                tmp.append(0) # 0으로 넣어줌
            else:
                tmp.append(arr[i][j])
        answer.append(tmp)
    return answer