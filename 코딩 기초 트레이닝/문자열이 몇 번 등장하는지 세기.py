# https://school.programmers.co.kr/learn/courses/30/lessons/181871?language=python3
def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        # 같다면
        if myString[i:i+len(pat)] == pat:
            answer += 1
    return answer