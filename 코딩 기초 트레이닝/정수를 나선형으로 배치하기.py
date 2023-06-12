# https://school.programmers.co.kr/learn/courses/30/lessons/181832?language=python3
def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    number, x1, y1, x2, y2 = 1, 0, 0, n-1, n-1
    
    while x1 <= x2 and y1 <= y2:
        # 왼 -> 오
        for y in range(y1,y2+1):
            answer[x1][y] = number
            number += 1
        x1 += 1
        
        # 위 -> 아래
        for x in range(x1,x2+1):
            answer[x][y2] = number
            number += 1
        y2 -= 1
        
        # 오 -> 왼
        for y in range(y2, y1-1, -1):
            answer[x2][y] = number
            number += 1
        x2 -= 1
        
        # 아래 -> 위
        for x in range(x2, x1-1, -1):
            answer[x][y1] = number
            number += 1
        y1 += 1
    return answer