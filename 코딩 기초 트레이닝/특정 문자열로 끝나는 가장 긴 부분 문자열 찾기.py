# https://school.programmers.co.kr/learn/courses/30/lessons/181872?language=python3
def solution(myString, pat):
    #print(myString[::-1].index(pat[::-1]))
    return myString[:len(myString) - myString[::-1].index(pat[::-1])]