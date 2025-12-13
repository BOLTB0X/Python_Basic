# 부모 클래스 (Parent Class)
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name}이 소리를 냅니다."

# 자식 클래스 (Child Class)가 Animal을 상속받음
class Dog(Animal):
    def bark(self): # Dog 클래스만의 새로운 메서드
        return f"{self.name}이 멍멍 짖습니다."

my_dog = Dog("바둑이")
print(my_dog.name)    # 부모 클래스에서 물려받은 속성
print(my_dog.speak()) # 부모 클래스에서 물려받은 메서드
print(my_dog.bark())  # 자식 클래스에서 추가된 메서드

class Parent1:
    def method1(self):
        return "Parent1의 메서드1"

class Parent2:
    def method2(self):
        return "Parent2의 메서드2"

class Child(Parent1, Parent2): # 괄호 안에 부모 클래스들을 콤마로 구분하여 나열
    def child_method(self):
        return "Child 클래스의 메서드"

child_obj = Child()
print(child_obj.method1()) # Parent1의 메서드 호출
print(child_obj.method2()) # Parent2의 메서드 호출
print(child_obj.child_method()) # Child 클래스의 메서드 호출

class ParentA:
    def common_method(self):
        return "나는 ParentA야"

class ParentB:
    def common_method(self):
        return "나는 ParentB야"

# ParentA를 먼저 상속 (ParentA의 메서드가 우선)
class Child(ParentA, ParentB):
    pass

child_a = Child()
print(child_a.common_method()) # 출력: 나는 ParentA야

# ParentB를 먼저 상속 (ParentB의 메서드가 우선)
class Child(ParentB, ParentA):
    pass

child_b = Child()
print(child_b.common_method()) # 출력: 나는 ParentB야
