# https://school.programmers.co.kr/learn/courses/30/lessons/181929?language=python3
def solution(num_list):
    mul = 1
    for n in num_list:
        mul *= n
    return int(mul < sum(num_list) ** 2)
