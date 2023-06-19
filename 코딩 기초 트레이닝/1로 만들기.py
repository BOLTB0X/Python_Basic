# https://school.programmers.co.kr/learn/courses/30/lessons/181880?language=python3
def solution(num_list):
    answer = 0
    for n in num_list:
        number = n
        while number != 1:
            if not number % 2:
                number = number // 2
            else:
                number = (number-1) // 2
            answer += 1
            
    return answer