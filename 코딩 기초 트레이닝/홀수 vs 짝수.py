# https://school.programmers.co.kr/learn/courses/30/lessons/181887?language=python3
def solution(num_list):
    return max(sum([num_list[i] for i in range(len(num_list)) if not i%2]),sum([num_list[i] for i in range(len(num_list)) if i%2]))