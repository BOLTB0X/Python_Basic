# https://school.programmers.co.kr/learn/courses/30/lessons/181884?language=python3
def solution(numbers, n):
    answer = 0
    for num in numbers:
        answer += num
        
        if answer > n:
            break
    return answer