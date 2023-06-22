# https://school.programmers.co.kr/learn/courses/30/lessons/181897?language=python3
def solution(n, slicer, num_list):
    answer = []
    if n == 1:
        for i in range(0,slicer[1]+1):
            answer.append(num_list[i])
    elif n == 2: 
        answer = num_list[slicer[0]:]
    elif n == 3:
        for i in range(slicer[0],slicer[1]+1):
            answer.append(num_list[i])
    else:
        for i in range(slicer[0],slicer[1]+1, slicer[2]):
            answer.append(num_list[i])
    return answer