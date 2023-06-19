# https://school.programmers.co.kr/learn/courses/30/lessons/181879?language=python3
def solution(num_list):
    answer = 1
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for n in num_list:
            answer *= n
    return answer