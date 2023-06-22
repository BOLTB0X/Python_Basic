# https://school.programmers.co.kr/learn/courses/30/lessons/181891?language=python3
def solution(num_list, n):
    answer = num_list
    
    for _ in range(n):
        answer.append(answer.pop(0))
    return answer