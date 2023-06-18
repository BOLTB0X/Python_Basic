# https://school.programmers.co.kr/learn/courses/30/lessons/181862?language=python3
def solution(myStr):
    answer = []
    
    tmp = "" # 임시
    for m in myStr:
        if m == "a" or m == "b" or m == "c":
            if len(tmp) > 0:
                answer.append(tmp)
                tmp = ""
            continue
        tmp += m
        
    if len(tmp) > 0:
        answer.append(tmp)
    else:
        answer.append("EMPTY")
    return answer