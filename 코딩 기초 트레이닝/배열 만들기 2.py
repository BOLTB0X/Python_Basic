# https://school.programmers.co.kr/learn/courses/30/lessons/181921
def check(num):
    if '1' in num or '2' in num or '3' in num or '4' in num or '6' in num or '7' in num or '8' in num or '9' in num:
        return False
    return True


def solution(l, r):
    answer = []

    for i in range(l, r+1):
        if i % 5 == 0 and check(str(i)):
            answer.append(i)

    if not answer:
        answer.append(-1)

    return answer
