# 그림 확대
def solution(picture, k):
    answer = []
    for p in picture:
        for _ in range(k):
            tmp = ""
            for pp in p:
                tmp += (pp*k)
            answer.append(tmp)
    return answer