# https://school.programmers.co.kr/learn/courses/30/lessons/181914
def solution(number):
    tot = 0
    for n in number:
        tot += int(n)
    return tot%9