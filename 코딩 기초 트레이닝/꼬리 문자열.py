# https://school.programmers.co.kr/learn/courses/30/lessons/181841?language=python3
def solution(str_list, ex):
    answer = ''
    
    for st in str_list:
        if ex in st: # 포함되어있다면
            continue
        answer += st
    return answer