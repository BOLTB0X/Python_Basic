# https://school.programmers.co.kr/learn/courses/30/lessons/181928?language=python3
def solution(num_list):
    tmp1, tmp2 = "", ""
    for n in num_list:
        if not n % 2:
            tmp1 += str(n)
        else:
            tmp2 += str(n)
    return int(tmp1)+int(tmp2)
