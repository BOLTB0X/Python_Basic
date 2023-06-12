# https://school.programmers.co.kr/learn/courses/30/lessons/181834?language=python3
def solution(myString):
    answer = ["l" if m < "l" else m for m in myString]
    return "".join(answer)