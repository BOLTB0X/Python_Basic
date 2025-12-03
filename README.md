# Python_Basic

![Python_img](https://s3.ap-northeast-2.amazonaws.com/grepp-cloudfront/programmers_imgs/learn/thumb-course-phthon-basic.jpg)

기초 문법 및 문제풀이

## 변수 & 자료형

<details>
<summary> 변수 (Variables) </summary>

<br/>

변수는 값을 저장하는 이름이 붙은 공간

#### 1. 변수 선언 및 할당

할당 연산자: `=` 사용

```py
age = 30
name = "B0X"
is_student = True
```

#### 2. 동적 타이핑 (Dynamic Typing)

파이썬의 가장 큰 특징 중 하나는 **동적 타이핑**

- 정의: 변수를 선언할 때 자료형을 명시적으로 지정할 필요가 없음, 파이썬 인터프리터가 값이 할당될 때 자동으로 자료형을 결정함

- 재할당: 하나의 변수에 다른 자료형의 값을 재할당할 수 있음

```py
x = 10      # x는 int(정수형)
x = "Hello" # x는 str(문자열) 로 변경됨
y = 3.14   # y는 float(실수형)
y = 2.718  # y는 float(실수형) 로 변경됨
```

#### 3. 변수 이름 규칙

**영문자, 숫자, 언더바(_)** 만 사용할 수 있음

- 숫자로 시작할 수 없음 (ex: `1st_name` (X), `name_1` (O))

- 대소문자를 구분 (`myVar`와 `myvar`는 다른 변수)

**예약어(Reserved Words)** 는 사용할 수 없음 (ex: `if`, `for`, `while`, `True` 등)

파이썬 권장 스타일 -> **스네이크 케이스(snake_case)** (ex: `user_name`, `total_score`)

<br/>


</details>

<details>
<summary> 자료형 (Data Types) </summary>

<br/>

#### 1. 기본 내장 자료형 (Primitive Types)

| 자료형 | 이름(Type) | 설명                   | ex                             |
| --- | -------- | -------------------- | ------------------------------ |
| 정수형 | `int`    | 소수점이 없는 숫자           | `10`, `-5`, `0`                |
| 실수형 | `float`  | 소수점이 있는 숫자           | `3.14`, `-0.001`, `2.0`        |
| 논리형 | `bool`   | 참(True) 또는 거짓(False) | `True`, `False`                |
| 문자열 | `str`    | 문자들의 나열 (따옴표로 묶음)    | `"Hello"`, `'Python'`, `"123"` |

#### 2. 컬렉션 자료형 특징 비교

| 자료형           | 특징                                              | 사용 ex                        |
| ------------- | ----------------------------------------------- | ---------------------------- |
| 리스트 (`list`)  | 순서 O, 중복 O, 수정 O (가변적)                          | `[1, 2, 3]`                  |
| 튜플 (`tuple`)  | 순서 O, 중복 O, 수정 X (불변적)                          | `(1, 2, 3)`                  |
| 딕셔너리 (`dict`) | 순서 X *(Python 3.7+ 에서는 입력 순서 유지)*, **키-값 쌍 저장** | `{"name": "Tom", "age": 20}` |
| 집합 (`set`)    | 순서 X, 중복 X                                      | `{1, 2, 3}`                  |


| 자료형           | 생성 기호                  | ex                 |
| ------------- | ---------------------- | ------------------ |
| 리스트 (`list`)  | 대괄호 `[]`               | `[1, 2, 3]`        |
| 튜플 (`tuple`)  | 소괄호 `()`               | `(1, 2, 3)`        |
| 딕셔너리 (`dict`) | 중괄호 `{}` + `Key:Value` | `{"a": 1, "b": 2}` |
| 집합 (`set`)    | 중괄호 `{}` (요소만)         | `{1, 2, 3}`        |

#### 3. 자료형 변환 (Type Conversion / Casting)

자주 특정 연산을 위해 변수의 자료형을 일시적 또는 영구적으로 바꿔야 할 때가 있음

- `int(x)` : $x$를 정수형으로 변환 (실수형일 경우 소수점 이하 버림)

- `float(x)` : $x$를 실수형으로 변환

- `str(x)` : $x$를 문자열로 변환

- `list(x)` , `tuple(x)` , `set(x)` : $x$를 각 컬렉션 자료형으로 변환

<br/>

</details>

## 조건문 & 반복문

<details>
<summary> 조건문 (Conditional Statements) </summary>

<br/>

특정 조건이 참(`True`)일 때만 코드를 실행하거나, 조건에 따라 다른 코드를 실행하도록 만들 때 사용

### 1. `if`, `elif`, `else` 구조

```py
if x > 10:
    ...
elif x == 10:
    ...
else:
    ...
```

- `if` (필수)

    - 가장 먼저 조건을 검사
    
    - 조건이 `True`이면 해당 블록을 실행
    
- `elif` (선택) 

    - `if` 조건이 `False`일 때, 다음으로 검사할 추가 조건을 지정 (0개 이상 사용 가능)
    
- `else` (선택)

    - `if` 와 모든 `elif` 조건이 모두 `False`일 때, 나머지 경우에 실행할 코드를 지정


- 문법 특징

    - 콜론 (`:`): 조건식 끝에는 반드시 콜론을 붙임

    - 들여쓰기 (Indentation): 조건이 참일 때 실행할 코드는 반드시 들여쓰기를 해야 함, 파이썬은 들여쓰기(일반적으로 공백 4칸)로 코드 블록을 구분

```py
# ex
score = 85

if score >= 90:
    print("A 학점입니다.")
elif score >= 80:
    print("B 학점입니다.")  # score가 85이므로 이 블록이 실행됨
elif score >= 70:
    print("C 학점입니다.")
else:
    print("F 학점입니다.")
```

### 2. 조건식에 사용되는 연산자

#### 비교연산자

| 종류 | 연산자       | 의미             |
| -- | --------- | -------------- |
| 비교 | `==`      | 값이 서로 같다       |
| 비교 | `!=`      | 값이 서로 다르다      |
| 비교 | `> , <`   | 크다, 작다         |
| 비교 | `>= , <=` | 크거나 같다, 작거나 같다 |


#### 논리연산자

| 종류 | 연산자   | 의미                                    |
| -- | ----- | ------------------------------------- |
| 논리 | `and` | 두 조건 모두 `True`일 때 True                  |
| 논리 | `or`  | 두 조건 중 하나라도 `True`일 때 True              |
| 논리 | `not` | 조건을 반전시킴 (`True` → `False`, `False` → `True`) |

<br/>


</details>


<details>
<summary> 반복문(Loops) </summary>

<br/>

<img src="https://github.com/BOLTB0X/Python_Basic/blob/main/Resoures/loop.png?raw=true" alt="Example Image" width="70%">
</p>

특정 코드 블록을 반복해서 실행할 때 사용됩

### 1. `for` 반복문

정해진 횟수만큼 또는 특정 컬렉션(리스트, 튜플, 문자열 등)의 모든 요소를 순회할 때 사용

```py
# 기본 구조 : 컬렉션 순회
ruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

`for` 문은 `range()` 함수와 함께 사용하여 정해진 횟수만큼 반복할 때 유용

```py
for i in range(5):
    print(f"현재 숫자: {i}")
```

| `range()` 형식                | 설명                 | 생성되는 숫자 시퀀스              |
| ------------------------- | ------------------ | ------------------------ |
| `range(n)`                | `0`부터 `n-1`까지 생성       | `0, 1, 2, ..., n-1`      |
| `range(start, end)`       | start부터 end-1까지 생성 | `start, ..., end-1`      |
| `range(start, end, step)` | step 간격으로 숫자 생성    | `start, start+step, ...` |

### 2. `while` 반복문

조건이 `True`인 동안 코드를 계속해서 반복 실행

언제 멈춰야 할지 명확하지 않고, 특정 조건이 충족될 때까지 무한정 반복해야 할 때 주로 사용

```py
count = 0

while count < 3:  # count가 3보다 작은 동안 반복
    print(f"반복 횟수: {count}")
    count += 1    # 1씩 증가시켜 언젠가 조건이 False가 되게 함
```

*cf. 무한 루프 (Infinite Loop)*

- *`while` 문의 조건이 **항상 True** 가 되면 프로그램이 끝나지 않고 무한히 반복됨*

- *반복문 내에서 조건을 `False`로 바꿀 수 있는 코드를 반드시 포함해야 함*

**흐름 제어 키워드**

- `break` (반복문 즉시 종료)

    `break` 를 만나면 현재 돌고 있는 `for` 나 `while` 반복문 자체를 완전히 빠져나감

- `continue` (현재 반복만 건너뛰기)

    `continue` 를 만나면 현재 반복 단계의 나머지 코드는 무시하고, 즉시 다음 반복 단계로 넘어감


```py
# ex
for number in range(10):
    if number % 2 != 0:
        continue  # 홀수이면 아래 코드를 건너뛰고 다음 반복으로
    
    if number >= 6:
        break     # 숫자가 6 이상이면 반복문 종료
        
    print(f"짝수입니다: {number}")

# 짝수입니다: 0
# 짝수입니다: 2
# 짝수입니다: 4
```

<br/>

</details>

<details>
<summary>  삼항 연산자 / 멤버십 연산자 / 식별 연산자 </summary>

<br/>

### 삼항 연산자 (Ternary Operator)

| 연산자    | 형식               | 의미                   |
| ------ | ---------------- | -------------------- |
| 삼항 연산자 | `A if 조건 else B` | 조건이 참이면 A, 거짓이면 B 반환 |

```py
result = "성인" if age >= 20 else "미성년자"
```

### 멤버십 연산자 (Membership Operator)

| 연산자      | 의미                                |
| -------- | --------------------------------- |
| `in`     | 값이 시퀀스(리스트, 문자열 등)에 포함되어 있으면 `True` |
| `not in` | 값이 시퀀스에 포함되어 있지 않으면 `True`         |

```py
3 in [1,2,3]         # True
"a" not in "hello"   # True
```

### 식별 연산자 (Identity Operator)

| 연산자      | 의미                               |
| -------- | -------------------------------- |
| `is`     | 두 객체가 **같은 객체**(동일한 메모리 주소)인지 확인 |
| `is not` | 두 객체가 **다른 객체**인지 확인             |

```py
a = [1,2,3]
b = a
c = [1,2,3]

a is b      # True (같은 객체)
a is c      # False (내용은 같지만 다른 객체)
```

<br/>


</details>

## 함수 & 모듈

<details>
<summary> 함수 (Functions) </summary>

<br/>

특정 작업을 수행하도록 설계된 코드 블록

복잡한 작업을 여러 개의 작은 함수로 나누면 코드를 이해하기 쉽고, 같은 작업을 반복해야 할 때 코드를 다시 작성할 필요 없이 함수만 호출하면 되므로 효율적

### 1. 함수의 정의 및 호출

함수는 `def` 키워드를 사용하여 정의

```py
def add(a, b):
    return a + b
```

- `def` : 함수 정의를 시작하는 키워드

- 함수 이름 : 함수를 호출할 때 사용하는 이름 (변수 이름 규칙과 동일)

- Parameter(ex: `a`, `b`) : 함수가 외부로부터 전달받는 입력 값 (선택 사항)

- `return` : 함수의 실행 결과를 **반환(출력)**하는 키워드 (선택 사항)

```py
def greet(name): # name: 매개변수
    """입력받은 이름으로 인사를 출력하는 함수"""
    message = f"안녕하세요, {name}님!"
    return message # 결과 값을 반환

result = greet("KyungHeon")
print(result) # 안녕하세요, KyungHeon님!
```

- 매개변수 (Parameter): 함수를 정의할 때 사용하는 변수 (`greet(name)`에서 `name`)

- 인자 (Argument): 함수를 호출할 때 전달하는 실제 값 (`greet("KyungHeon")`에서 `"KyungHeon"`)


### 2. 반환 값 (`return`)

- `return` 문은 함수의 결과 값을 호출한 곳으로 반환

- `return` 을 만나면 함수는 즉시 실행을 종료

- `return` 문이 없거나 `return` 뒤에 아무것도 없으면, 파이썬은 자동으로 **None**을 반환

### 3. 가변인자

#### 위치 가변 인자(`*args`)

```py
def func(*args):      # tuple
    print(args)
```

임의의 개수의 인자를 받는 함수를 가리켜 가변 인자를 사용한다고 표현

```py
# ex
def f(x, *args):
    ...
```

- `x` -> `1`

- `args` -> `(2,3,4,5)`

- 튜플로 전달

```py
f(1,2,3,4,5)
```

#### 키워드 가변 인자(`**kwargs`)

```py
def func2(**kwargs):  # dict
    print(kwargs)
```

함수는 임의의 개수의 키워드 인자도 받을 수 있음

```py
def f(x, y, **kwargs):
    ...
```

- `x` -> `2`

- `y` -> `3`

- `kwargs` -> `{ 'flag': True, 'mode': 'fast', 'header': 'debug' }`

```py
f(2, 3, flag=True, mode='fast', header='debug')
```

#### 두 가지를 혼합

```py
def f(*args, **kwargs):
```

함수는 임의의 개수의 가변 인자와 키워드 없는(non-keyword) 인자들을 받을 수 있음

<br/>

</details>

<details>
<summary> 모듈 (Module) </summary>

<br/>

모듈은 함수, 변수, 클래스 등을 모아 놓은 하나의 파이썬 파일임

`.py` 확장자를 가진 파일 하나하나가 모듈이 될 수 있음

### 1. 모듈 생성

```py
# math_operations.py
def multiply(x, y):
    return x * y

def power(x, y):
    return x ** y
```

### 2. 모듈 불러오기 (`import`)

| import 문                | 설명                                                | 사용 예시                                                       |
| ----------------------- | ------------------------------------------------- | ----------------------------------------------------------- |
| `import 모듈이름`           | 모듈 전체를 불러옴.<br>사용할 때 `모듈이름.함수()` 형식으로 접근해야 함.     | `import math_operations` → `math_operations.multiply(2, 4)` |
| `from 모듈이름 import 함수이름` | 모듈에서 특정 함수/변수만 가져옴.<br>모듈 이름 없이 바로 `함수()`로 사용 가능. | `from math_operations import power` → `power(2, 3)`         |
| `import 모듈이름 as 별칭`     | 모듈에 **별칭(alias)**을 지정하여 이름을 짧게 줄여 사용.             | `import math_operations as mo` → `mo.multiply(5, 5)`        |


```py
import math_operations as mo

# 모듈의 함수 호출
result_mult = mo.multiply(10, 5) # 50
print(result_mult) 

from math_operations import power

result_power = power(2, 4) # 16
print(result_power)
```

### 3. 표준 모듈 (Standard Modules)

- `math` : 수학 함수 (제곱근, 삼각 함수, 로그 등)

- `random` : 난수(무작위 숫자) 생성 기능

- `os` : 운영체제와 상호작용하는 기능 (파일 및 디렉토리 제어 등)

```py
import math

root = math.sqrt(25)
print(root)
```

<br/>

</details>

<details>
<summary> 람다(Lambda) </summary>

<br/>

### 1. 익명 함수

일반적인 함수는 `def` 키워드로 정의하고 이름을 붙이지만, 람다 함수는 이름이 없음

이 때문에 **익명 함수** 라고 불림

### 2. 구조적 특징

- 단일 표현식

    -  **람다 함수** 는 오직 하나의 **표현식(expression)** 만을 포함해야 하며, 이 표현식의 결과가 자동으로 반환됌
    
    - `if`, `for`, `while` 같은 **문장(statement)** 은 사용할 수 없음

- 간결성

### 3. 문법 (Syntax)

```py
lambda 인자1, 인자2, ...: 표현식
```

- `lambda` : 람다 함수를 정의하는 키워드 (일반 함수의 def 역할)

- 인자 : 함수가 받을 입력 값 (0개 이상)

- `:` : 인자와 표현식을 구분하는 콜론

- 표현식 : 함수가 수행할 작업 및 반환 값

### 4. 람다 함수 사용 예시

**일반 함수와 람다 함수 비교**

```py
# 일반 함수
def add(x, y):
    return x + y
result = add(3, 5)
```

```py
# 람다 ex
add_lambda = lambda x, y: x + y

result = add_lambda(3, 5)
```

**인자 없는 람다**

```py
get_pi = lambda: 3.14159
print(get_pi())
```

1. `sorted()` 에서 사용

    `sorted()` 함수는 리스트를 정렬할 때, 정렬의 기준(key)을 지정하기 위해 함수를 인자로 받음

    ```py
    # 이름과 나이를 가진 튜플 리스트
    students = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]

    # 나이(튜플의 두 번째 요소, 인덱스 1)를 기준으로 정렬
    sorted_by_age = sorted(students, key=lambda student: student[1])

    print(sorted_by_age)
    # [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
    ```

    ---

2. `filter()` 에서 사용

    `filter()` 함수는 시퀀스(리스트 등)에서 특정 조건이 `True` 인 요소만 필터링하여 반환

    ```py
    numbers = [1, 2, 3, 4, 5, 6]

    # 짝수만 걸러내는 람다 함수
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    print(even_numbers)
    # [2, 4, 6]
    ```

    ---

3. `map()`에서 사용

    `map()` 함수는 시퀀스의 모든 요소에 대해 특정 함수를 적용하고 그 결과를 반환

    ```py
    numbers = [1, 2, 3, 4]

    # 모든 요소에 10을 곱하는 람다 함수
    multiplied = list(map(lambda x: x * 10, numbers))

    print(multiplied)
    # [10, 20, 30, 40]
    ```

    ----

### 5. 람다 함수의 한계

- **복잡한 로직 불가** : 여러 줄의 코드나 복잡한 조건/반복문이 필요한 작업에는 사용할 수 없음

- 가독성: 너무 복잡한 람다 표현식은 오히려 일반 `def` 함수보다 읽기 어려울 수 있음

<br/>

</details>


## 참고

- [위키독스](https://wikidocs.net/)