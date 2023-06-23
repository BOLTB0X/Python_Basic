# https://school.programmers.co.kr/learn/courses/30/lessons/181904?language=python3
def solution(my_string, m, c):
    answer = ''

    for i in range(c-1,len(my_string),m):
        answer += my_string[i]
    return answer