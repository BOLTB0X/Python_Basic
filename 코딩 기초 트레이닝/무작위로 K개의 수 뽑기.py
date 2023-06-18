# https://school.programmers.co.kr/learn/courses/30/lessons/181858
def solution(arr, k):
    answer = []
    
    for i in range(len(arr)):
        # 중복 방지
        if not arr[i] in answer:
            answer.append(arr[i])
        
        if len(answer) == k:
            break

    return answer + [-1] * (k-len(answer))