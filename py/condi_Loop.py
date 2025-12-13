score = 85

if score >= 90:
    print("A 학점입니다.")
elif score >= 80:
    print("B 학점입니다.") 
elif score >= 70:
    print("C 학점입니다.")
else:
    print("F 학점입니다.")

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)


for i in range(5):
    print(f"현재 숫자: {i}")

count = 0

while count < 3:  # count가 3보다 작은 동안 반복
    print(f"반복 횟수: {count}")
    count += 1    # 1씩 증가시켜 언젠가 조건이 False가 되게 함

# 반복 횟수: 0
# 반복 횟수: 1
# 반복 횟수: 2

for number in range(10):
    if number % 2 != 0:
        continue  # 홀수이면 아래 코드를 건너뛰고 다음 반복으로
    
    if number >= 6:
        break     # 숫자가 6 이상이면 반복문 종료
        
    print(f"짝수입니다: {number}")

# 짝수입니다: 0
# 짝수입니다: 2
# 짝수입니다: 4

a = [1,2,3]
b = a
c = [1,2,3]

print(a is b)     # True (같은 객체)
print(a is c)      # False (내용은 같지만 다른 객체)
