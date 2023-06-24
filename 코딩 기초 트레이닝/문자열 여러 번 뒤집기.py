# https://school.programmers.co.kr/learn/courses/30/lessons/181913
def solution(my_string, queries):
    answer = my_string
    for q in queries:
        answer = answer[:q[0]] + answer[q[0]:q[1]+1][::-1] + answer[q[1]+1:]
    return answer