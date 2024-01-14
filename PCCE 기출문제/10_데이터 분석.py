# https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    answer = []
        
    for d in data:
        if ext == "code" and d[0] < val_ext:
            answer.append(d)

        elif ext == "date" and d[1] < val_ext:
            answer.append(d)
        
        elif ext == "maximum" and d[2] < val_ext:
            answer.append(d)
            
        elif ext == "remain" and d[3] < val_ext:
            answer.append(d)
    
    if sort_by == "code":
        answer.sort(key=lambda x : x[0])
        
    elif sort_by == "date":
        answer.sort(key=lambda x : x[1])
        
    elif sort_by == "maximum":
        answer.sort(key=lambda x : x[2])
        
    elif sort_by == "remain":
        answer.sort(key=lambda x : x[3])
            
    return answer