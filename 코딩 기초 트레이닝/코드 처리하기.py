# https://school.programmers.co.kr/learn/courses/30/lessons/181932?language=python3
def solution(code):
    answer = ''
    mode = 0

    for i in range(len(code)):
        if "1" == code[i]:
            mode = 1 if mode == 0 else 0
        else:
            if mode == 0 and not i % 2:
                answer += code[i]
            elif mode == 1 and i % 2:
                answer += code[i]
    return answer if len(answer) > 0 else "EMPTY"
