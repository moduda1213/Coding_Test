# 파이썬 `re` 정규식 기초

정규식(Regular Expression)은 문자열에서 일정한 규칙을 가진 부분을 찾거나, 검사하거나, 바꾸는 방법입니다.

파이썬에서는 `re` 모듈을 불러와 사용합니다.

```python
import re
```

정규식 문자열에는 역슬래시(`\`)가 자주 사용되므로 일반적으로 문자열 앞에 `r`을 붙입니다.

```python
pattern = r"\d+"
```

## 1. `re.search()` — 처음 일치하는 부분 찾기

문자열 전체에서 정규식과 처음 일치하는 부분을 찾습니다. 일치하는 부분이 없으면 `None`을 반환합니다.

```python
import re

text = "주문 번호는 2025번입니다."
match = re.search(r"\d+", text)

if match:
    print(match.group())  # 2025
    print(match.start())  # 시작 인덱스
    print(match.end())    # 끝 다음 인덱스
    print(match.span())   # (시작 인덱스, 끝 다음 인덱스)
```

`search()`는 문자열 중간에 있는 패턴도 찾습니다.

## 2. `re.fullmatch()` — 문자열 전체 형식 검사하기

문자열 전체가 정규식과 일치하는지 검사합니다.

```python
import re

phone = "010-1234-5678"
pattern = r"\d{3}-\d{4}-\d{4}"

if re.fullmatch(pattern, phone):
    print("올바른 전화번호 형식입니다.")
else:
    print("올바르지 않은 형식입니다.")
```

아이디, 전화번호, 이메일 등 입력값 전체의 형식을 검사할 때 유용합니다.

## 3. `re.findall()` — 일치하는 모든 값 찾기

정규식과 일치하는 모든 문자열을 리스트로 반환합니다.

```python
import re

text = "사과 3개, 바나나 12개, 포도 5개"
numbers = re.findall(r"\d+", text)

print(numbers)  # ['3', '12', '5']
```

반환된 숫자는 문자열이므로 계산하려면 정수로 변환해야 합니다.

```python
numbers = list(map(int, re.findall(r"\d+", text))) # 숫자하나
print(sum(numbers))  # 20
```

## 4. `re.finditer()` — 값과 위치를 함께 찾기

일치하는 각 결과를 반복 가능한 형태로 반환합니다. 문자열뿐 아니라 시작·종료 위치도 확인할 수 있습니다.

```python
import re

text = "apple banana grape"

for match in re.finditer(r"\S+", text): # 공백 제외 문자 반복
    print(match.group(), match.start(), match.end())
```

출력:

```text
apple 0 5
banana 6 12
grape 13 18
```

`end()`는 마지막 문자의 위치가 아니라 마지막 문자 다음 위치를 반환합니다.

## 5. `re.sub()` — 일치하는 부분 바꾸기

정규식과 일치하는 모든 부분을 다른 문자열로 바꿉니다.

```python
import re

text = "전화번호는 010-1234-5678입니다."
result = re.sub(r"\d{3}-\d{4}-\d{4}", "[전화번호]", text) # 숫자 {n}번 반복

print(result)
# 전화번호는 [전화번호]입니다.
```

연속된 공백을 하나로 정리할 수도 있습니다.

```python
text = "hello     python   world"
result = re.sub(r"\s+", " ", text) # \s 공백 포함 문자

print(result)  # hello python world
```

## 6. `re.split()` — 여러 구분자로 문자열 나누기

정규식과 일치하는 부분을 구분자로 사용해 문자열을 나눕니다.

```python
import re

text = "apple,banana;grape orange"
words = re.split(r"[,; ]+", text)

print(words)
# ['apple', 'banana', 'grape', 'orange']
```

공백만 기준으로 나눌 때는 정규식보다 `text.split()`이 간단합니다. 쉼표, 세미콜론, 공백처럼 여러 구분자를 함께 처리할 때 `re.split()`을 사용하면 좋습니다.

## 자주 사용하는 정규식 기호

| 표현 | 의미 | 예시 |
| --- | --- | --- |
| `.` | 임의의 문자 한 개 | `a.c`는 `abc`, `axc`와 일치 |
| `\d` | 숫자 한 개 | `0`부터 `9` |
| `\D` | 숫자가 아닌 문자 한 개 | `a`, `#` |
| `\w` | 문자, 숫자 또는 밑줄 | `abc_123` |
| `\W` | 문자, 숫자, 밑줄이 아닌 문자 | 공백, `!` |
| `\s` | 공백 문자 | 공백, 탭, 줄바꿈 |
| `\S` | 공백이 아닌 문자 | 단어 등 |
| `^` | 문자열의 시작 | `^Hello` |
| `$` | 문자열의 끝 | `world$` |
| `[abc]` | `a`, `b`, `c` 중 한 문자 | `[0-9]`는 숫자 한 개 |
| `[^abc]` | `a`, `b`, `c`가 아닌 문자 | `[^0-9]`는 숫자가 아닌 문자 |
| `*` | 앞 패턴이 0번 이상 반복 | `a*` |
| `+` | 앞 패턴이 1번 이상 반복 | `\d+` |
| `?` | 앞 패턴이 0번 또는 1번 | `-?` |
| `{n}` | 앞 패턴이 정확히 `n`번 반복 | `\d{3}` |
| `{n,m}` | 앞 패턴이 `n`번 이상 `m`번 이하 반복 | `\d{2,4}` |
| `()` | 패턴 묶기 또는 그룹 추출 | `(010)-(\d{4})` |
| `\|` | 양쪽 패턴 중 하나 | `cat\|dog` |

## 그룹으로 원하는 부분 추출하기

괄호 `()`로 패턴을 묶으면 일치한 문자열에서 원하는 부분을 따로 가져올 수 있습니다.

```python
import re

phone = "010-1234-5678"
match = re.fullmatch(r"(\d{3})-(\d{4})-(\d{4})", phone)

if match:
    print(match.group())   # 010-1234-5678
    print(match.group(1))  # 010
    print(match.group(2))  # 1234
    print(match.group(3))  # 5678
```

---

# 연습문제

먼저 힌트와 모범 답안을 보지 않고 풀어보세요.

## 문제 1. 숫자 모두 찾기

다음 문자열에서 숫자를 모두 찾아 리스트로 출력하세요.

```python
text = "상품 A는 1200원, 상품 B는 3500원, 배송비는 500원입니다."
```

예상 결과:

```python
['1200', '3500', '500']
```

## 문제 2. 아이디 형식 검사하기

아이디가 다음 조건을 만족하는지 검사하세요.

- 영문 소문자로 시작한다.
- 영문 소문자와 숫자만 사용할 수 있다.
- 전체 길이는 5자 이상 10자 이하이다.

```python
user_ids = ["python7", "7python", "py!hon", "algorithm123"]
```

각 아이디에 대해 `True` 또는 `False`를 출력하세요.

## 문제 3. 연속된 공백 정리하기

다음 문자열의 연속된 공백을 공백 하나로 변경하세요.

```python
text = "Python     regular   expression    practice"
```

예상 결과:

```text
Python regular expression practice
```

## 문제 4. 여러 구분자로 문자열 나누기

쉼표, 세미콜론, 콜론 또는 하나 이상의 공백을 기준으로 문자열을 나누세요.

```python
text = "apple,banana;grape:orange  melon"
```

예상 결과:

```python
['apple', 'banana', 'grape', 'orange', 'melon']
```

## 문제 5. 단어와 위치 출력하기

`re.finditer()`를 이용해 각 단어와 `[시작 인덱스, 마지막 인덱스]`를 출력하세요.

```python
text = "hello python world"
```

예상 결과:

```text
hello [0, 4]
python [6, 11]
world [13, 17]
```

주의: `match.end()`는 마지막 글자 다음 위치를 반환합니다.

## 문제 6. 스포일러 범위에 걸친 단어 찾기

다음 문장에서 스포일러 범위와 한 글자 이상 겹치는 단어를 모두 찾으세요. 범위의 `start`와 `end`는 모두 포함되는 인덱스입니다.

```python
text = "hello python world"
spoiler_ranges = [[3, 8], [14, 15]]
```

조건:

- `[3, 8]`은 `hello`와 `python`에 걸쳐 있습니다.
- `[14, 15]`는 `world`에 포함됩니다.
- 같은 단어의 동일한 등장 위치가 여러 범위와 겹쳐도 한 번만 추가합니다.

예상 결과:

```python
['hello', 'python', 'world']
```

---

# 힌트

## 문제 1 힌트

숫자가 한 번 이상 반복되는 패턴 `\d+`와 `re.findall()`을 사용합니다.

## 문제 2 힌트

문자열 전체를 검사하는 `re.fullmatch()`를 사용합니다. 첫 글자와 나머지 글자의 패턴을 나누어 생각해 보세요.

## 문제 3 힌트

공백이 한 번 이상 반복되는 `\s+`를 공백 하나로 바꿉니다.

## 문제 4 힌트

문자 집합 `[]` 안에 구분자를 넣고, 뒤에 `+`를 붙입니다.

## 문제 5 힌트

공백이 아닌 문자가 한 번 이상 반복되는 패턴은 `\S+`입니다. 마지막 인덱스는 `match.end() - 1`입니다.

## 문제 6 힌트

단어 범위를 `[word_start, word_end)`로 표현했을 때 두 범위의 겹침 조건은 다음과 같습니다.

```python
word_start <= range_end and range_start < word_end
```

한 단어를 찾은 뒤 내부 반복문을 `break`하면 같은 등장 위치의 중복 추가를 막을 수 있습니다.

---

# 모범 답안

## 문제 1 답안

```python
import re

text = "상품 A는 1200원, 상품 B는 3500원, 배송비는 500원입니다."
numbers = re.findall(r"\d+", text)

print(numbers)
```

## 문제 2 답안

```python
import re

user_ids = ["python7", "7python", "py!hon", "algorithm123"]
pattern = r"[a-z][a-z0-9]{4,9}"

for user_id in user_ids:
    print(user_id, bool(re.fullmatch(pattern, user_id)))
```

첫 글자 `[a-z]` 한 자와 나머지 `[a-z0-9]` 4~9자를 합치면 전체 길이는 5~10자가 됩니다.

## 문제 3 답안

```python
import re

text = "Python     regular   expression    practice"
result = re.sub(r"\s+", " ", text)

print(result)
```

## 문제 4 답안

```python
import re

text = "apple,banana;grape:orange  melon"
words = re.split(r"[,;:\s]+", text)

print(words)
```

## 문제 5 답안

```python
import re

text = "hello python world"

for match in re.finditer(r"\S+", text):
    print(f"{match.group()} [{match.start()}, {match.end() - 1}]")
```

## 문제 6 답안

```python
import re

text = "hello python world"
spoiler_ranges = [[3, 8], [14, 15]]
find_words = []

for match in re.finditer(r"\S+", text):
    word = match.group()
    word_start = match.start()
    word_end = match.end()

    for range_start, range_end in spoiler_ranges:
        if word_start <= range_end and range_start < word_end:
            find_words.append(word)
            break

print(find_words)
```

## 다음 학습 순서

이 자료의 문제를 모두 풀었다면 다음 내용을 순서대로 익혀보세요.

1. 그룹 `()`과 `group(1)`, `group(2)` 사용하기
2. 이름 있는 그룹 `(?P<name>...)` 사용하기
3. 탐욕적 수량자 `.*`와 비탐욕적 수량자 `.*?`의 차이
4. `re.IGNORECASE`, `re.MULTILINE` 같은 정규식 옵션
5. 반복해서 사용하는 정규식을 `re.compile()`로 미리 만들기
