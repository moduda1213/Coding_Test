# 파이썬의 Argument Unpacking 정리

## 1. `*`는 C/C++의 포인터 연산자가 아니다

C/C++에서 `*`는 포인터를 선언하거나 포인터가 가리키는 값에 접근할 때 사용한다.

```cpp
int value = 10;
int* pointer = &value;
cout << *pointer;
```

파이썬에는 이와 같은 포인터 문법이 없다. 파이썬에서 `*`는 사용되는 위치에 따라 여러 값을 **펼치거나(unpacking)** 여러 값을 **모으는(packing)** 역할을 한다.

## 2. 함수 호출에서 값 펼치기

리스트나 튜플 앞에 `*`를 붙여 함수에 전달하면, 각 원소가 별도의 위치 인자로 전달된다.

```python
numbers = [1, 2, 3]

print(*numbers)
# print(1, 2, 3)과 같다.
# 출력: 1 2 3
```

다음 두 함수 호출도 같은 의미이다.

```python
max(*numbers)
max(1, 2, 3)
```

이를 **argument unpacking** 또는 **인자 언패킹**이라고 한다.

## 3. `zip(files)`의 동작

파일의 좌표가 다음과 같이 저장되어 있다고 가정하자.

```python
files = [(0, 1), (0, 2), (1, 0)]
```

`zip(files)`는 `zip()`에 `files`라는 인자를 하나만 전달한다.

```python
result = list(zip(files))
print(result)
```

결과는 다음과 같다.

```python
[((0, 1),), ((0, 2),), ((1, 0),)]
```

`zip()`은 전달받은 각 iterable에서 같은 순서의 값을 하나씩 꺼내 묶는다. 하지만 전달된 iterable이 `files` 하나뿐이므로 각 좌표가 길이 1인 튜플로 감싸진다.

따라서 다음 코드는 오류가 발생한다.

```python
rows, cols = zip(files)
```

오른쪽에서는 세 개의 값이 나오지만, 왼쪽에는 값을 받을 변수가 두 개뿐이기 때문이다.

```text
ValueError: too many values to unpack (expected 2)
```

좌표가 정확히 두 개라면 오류는 발생하지 않지만, 행과 열이 분리되는 것도 아니다.

```python
files = [(0, 1), (2, 3)]
rows, cols = zip(files)

print(rows)  # ((0, 1),)
print(cols)  # ((2, 3),)
```

## 4. `zip(*files)`의 동작

`*files`는 리스트 안의 좌표 튜플들을 `zip()`의 개별 인자로 펼친다.

```python
files = [(0, 1), (0, 2), (1, 0)]
zip(*files)
```

위 호출은 다음과 같다.

```python
zip((0, 1), (0, 2), (1, 0))
```

`zip()`이 각 튜플에서 같은 위치의 값을 묶으므로 다음 결과가 만들어진다.

```python
list(zip(*files))
# [(0, 0, 1), (1, 2, 0)]
```

- 첫 번째 튜플 `(0, 0, 1)`은 모든 행 번호이다.
- 두 번째 튜플 `(1, 2, 0)`은 모든 열 번호이다.

따라서 두 변수에 다음과 같이 나누어 담을 수 있다.

```python
rows, cols = zip(*files)

print(rows)  # (0, 0, 1)
print(cols)  # (1, 2, 0)
```

이처럼 행렬의 행과 열을 서로 바꾸는 형태의 작업을 **전치(transpose)**라고 한다.

## 5. 바탕화면 정리 문제에 적용하기

모든 `#`의 좌표를 구한 뒤 행과 열을 분리할 수 있다.

```python
def solution(wallpaper):
    files = [
        (row, col)
        for row, line in enumerate(wallpaper)
        for col, cell in enumerate(line)
        if cell == "#"
    ]

    rows, cols = zip(*files)

    return [
        min(rows),
        min(cols),
        max(rows) + 1,
        max(cols) + 1,
    ]
```

예를 들어 다음과 같은 좌표가 있다면:

```python
files = [(0, 1), (0, 2), (1, 0)]
```

행과 열은 다음처럼 분리된다.

```python
rows = (0, 0, 1)
cols = (1, 2, 0)
```

가장 작은 행과 열, 가장 큰 행과 열을 이용해 모든 파일을 포함하는 영역을 구할 수 있다.

```python
[min(rows), min(cols), max(rows) + 1, max(cols) + 1]
# [0, 0, 2, 3]
```

## 6. 대입문에서 여러 값 모으기

대입문의 변수 앞에 `*`를 붙이면 남은 값들을 리스트로 모아서 받는다.

```python
first, *middle, last = [1, 2, 3, 4, 5]

print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

함수 호출에서는 값을 펼쳤지만, 대입문에서는 여러 값을 하나로 모은다는 차이가 있다.

## 7. 함수 정의에서 `*args` 사용하기

함수를 정의할 때 `*args`를 사용하면 전달된 여러 위치 인자를 튜플로 모아서 받을 수 있다.

```python
def add_all(*args):
    print(args)
    return sum(args)


print(add_all(1, 2, 3))
# args: (1, 2, 3)
# 결과: 6
```

호출할 때의 `*`와 함수 정의에서의 `*args`는 서로 반대 방향으로 생각할 수 있다.

```python
numbers = [1, 2, 3]
add_all(*numbers)  # 리스트를 개별 인자로 펼친다.
```

```python
def add_all(*args):  # 개별 인자를 튜플로 모은다.
    return sum(args)
```

## 8. 빈 리스트에 대한 주의

`files`가 비어 있으면 `zip(*files)`의 결과에도 값이 없다.

```python
files = []
rows, cols = zip(*files)
```

이 경우 두 변수에 넣을 값이 없으므로 다음 오류가 발생한다.

```text
ValueError: not enough values to unpack (expected 2, got 0)
```

빈 입력이 가능하다면 먼저 확인해야 한다.

```python
if not files:
    return []

rows, cols = zip(*files)
```

바탕화면 정리 문제에서 `#`이 하나 이상 존재한다고 보장한다면 이 검사는 생략할 수 있다.

## 9. 핵심 정리

```text
함수 호출의 *values    iterable의 원소들을 개별 위치 인자로 펼친다.
대입문의 *rest         남은 값들을 리스트로 모은다.
함수 정의의 *args      여러 위치 인자를 튜플로 모은다.
zip(files)             files 하나만 zip()에 전달한다.
zip(*files)            files의 각 원소를 zip()의 개별 인자로 전달한다.
```

`zip(*files)`는 좌표 목록에서 행과 열을 분리하는 전치 작업으로 이해하면 된다.
