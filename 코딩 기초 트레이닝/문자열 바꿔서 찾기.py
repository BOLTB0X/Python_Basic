# https://school.programmers.co.kr/learn/courses/30/lessons/181864?language=python3
def switchAB(alp):
    return "A" if alp == "B" else "B"

def solution(myString, pat):
    myStr = list(myString)
    
    for i in range(len(myStr)):
        myStr[i] = switchAB(myStr[i])
    
    myStr = ''.join(myStr) # 다시 문자열로
    
    if pat in myStr:
        return 1
    return 0