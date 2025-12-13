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
    count = 0

    def __init__(self, name, age): # 생성자: 객체가 만들어질 때 호출됨
        self.name = name         # self.name은 이 객체만의 name 속성
        self.age = age           # self.age는 이 객체만의 age 속성

    def introduce(self):         # 인스턴스 메서드
        print(f"안녕하세요, 저는 {self.name}이고 {self.age}살입니다.") # self를 통해 name과 age 접근

    @property # getter for 'name'
    def name(self):
        print("Getter for name called.")
        return self._name

    @name.setter # setter for 'name'
    def name(self, new_name):
        print(f"Setter for name called with: {new_name}")
        if len(new_name) > 0:
            self._name = new_name
        else:
            print("이름은 비어있을 수 없습니다.")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and 0 <= value <= 120:
            self._age = value
        else:
            print("잘못된 나이 값입니다.")


p1 = Person("김철수", 34)
p2 = Person("박영희", 93)

p1.introduce()
# 안녕하세요, 저는 김철수이고 34살입니다.
p2.introduce()
# 안녕하세요, 저는 박영희이고 93살입니다.

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self): # self를 받음
        print(f"{self.name} says 멍멍!")

    species = "Canis familiaris" # 클래스 변수
    
    @classmethod
    def get_species(cls): # cls를 받음
        return cls.species

print(Dog.get_species())
# Canis familiaris

class Calculator:
    @staticmethod
    def add(x, y): # self나 cls를 받지 않음
        return x + y

print(Calculator.add(10, 5))


p = Person("Alice", 30)

# getter 호출 (속성 접근처럼)
print(p.name) # Getter for name called. -> Alice
print(p.age)  # 30

# setter 호출 (속성 할당처럼)
p.name = "Bob" # Setter for name called with: Bob
print(p.name)  # Getter for name called. -> Bob

p.age = 150    # 잘못된 나이 값입니다.
print(p.age)   #  30

p.age = 25 
print(p.age)