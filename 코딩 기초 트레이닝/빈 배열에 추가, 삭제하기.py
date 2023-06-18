# https://school.programmers.co.kr/learn/courses/30/lessons/181860?language=python3
def solution(arr, flag):
    answer = []
    
    for i in range(len(arr)):
        if flag[i]:
            tmp = [arr[i]] * (arr[i]*2)
            answer += tmp
        else:
            if len(answer) > 0:
                for _ in range(arr[i]):
                    answer.pop()
    return answer