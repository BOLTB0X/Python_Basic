class ClassName:
    # 생성자
    def __init__(self, parameter1, parameter2):
        self.parameter1 = parameter1
        self.parameter2 = parameter2

    # 메서드
    def method(self):
        print(self.parameter1, self.parameter2)

obj = ClassName(3, 4)

class Person:
    def __init__(self, name, age): # 생성자: 객체가 만들어질 때 호출됨
        self.name = name         # self.name은 이 객체만의 name 속성
        self.age = age           # self.age는 이 객체만의 age 속성

    def introduce(self):         # 인스턴스 메서드
        print(f"안녕하세요, 저는 {self.name}이고 {self.age}살입니다.") # self를 통해 name과 age 접근

p1 = Person("김철수", 34)
p2 = Person("박영희", 93)

p1.introduce()
# 안녕하세요, 저는 김철수이고 34살입니다.
p2.introduce()
# 안녕하세요, 저는 박영희이고 93살입니다.