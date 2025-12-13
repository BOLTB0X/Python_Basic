def greet(name): # name: 매개변수
    """입력받은 이름으로 인사를 출력하는 함수"""
    message = f"안녕하세요, {name}님!"
    return message # 결과 값을 반환

# 함수의 호출
result = greet("KyungHeon")
print(result) # 출력: 안녕하세요, KyungHeon님!

import math_operations as mo

# 모듈의 함수 호출
result_mult = mo.multiply(10, 5) # 50
print(result_mult) 

from math_operations import power

result_power = power(2, 4) # 16
print(result_power)

import math

root = math.sqrt(25)
print(root)

students = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]

sorted_by_age = sorted(students, key=lambda student: student[1])

print(sorted_by_age)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)