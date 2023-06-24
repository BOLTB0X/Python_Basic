# https://school.programmers.co.kr/learn/courses/30/lessons/181915
def solution(my_string, index_list):
    answer = ''
    for idx in index_list:
        answer += my_string[idx]
    return answer