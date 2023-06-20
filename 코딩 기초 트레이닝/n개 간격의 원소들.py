# https://school.programmers.co.kr/learn/courses/30/lessons/181888?language=python3
def solution(num_list, n):
    return [num_list[i] for i in range(0,len(num_list),n)]