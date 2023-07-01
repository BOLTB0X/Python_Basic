# https://school.programmers.co.kr/learn/courses/30/lessons/181949?language=python3
str = input()

answer = ""

for a in str:
    if a.isupper():
        answer += a.lower()
    else:
        answer += a.upper()

print(answer)
