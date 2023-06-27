# https://school.programmers.co.kr/learn/courses/30/lessons/181919?language=python3
def solution(n):
    answer = [n]

    while n > 1:
        if not n % 2:
            answer.append(n // 2)
            n //= 2
        else:
            answer.append(3*n+1)
            n = 3*n + 1
    return answer
