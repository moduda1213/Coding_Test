import re

# 문제 1
text = "상품 A는 1200원, 상품 B는 3500원, 배송비는 500원입니다."
synt = re.findall(r'\d+', text)
print(f"문제 1. {synt}")
print("-----------------------------------------------------------")
# 문제 2
user_ids = ["python7", "7python", "py!hon", "algorithm123"]
# - 영문 소문자로 시작한다.
# - 영문 소문자와 숫자만 사용할 수 있다.
# - 전체 길이는 5자 이상 10자 이하이다.
pattern = r"^[a-z][a-z0-9]{4,9}$"
result = {}
print("문제 2.")
for user_id in user_ids:
    print(user_id, bool(re.fullmatch(pattern,user_id)))
print("-----------------------------------------------------------")
# 문제 3
text = "Python     regular   expression    practice"
result = re.sub(r"\s+", " ", text)
print(f"문제 3. {result}")
print("-----------------------------------------------------------")
# 문제 4
text = "apple,banana;grape:orange  melon"
result = re.split(r"[,;:\s]+", text)
print(f"문제 4. {result}")
print("-----------------------------------------------------------")
# 문제 5
text = "hello python world"
# results = re.finditer(r"\S+", text)
# for result in results:
#     # `match.end()`는 마지막 글자 다음 위치를 반환합니다.
#     print(f"{result.group()} [{result.start()} {result.end()-1}]")
print("문제 5.")
for match in re.finditer(r"\S+", text):
    print(f"{match.group()} [{match.start()} {match.end() - 1}]")
    
print("-----------------------------------------------------------")
# 문제 6
text = "hello python world"
spoiler_ranges = [[3, 8], [14, 15]]

words = text.split(" ")
result = set()
for target in re.finditer(r"\S+", text):
    target_name = target.group()
    target_start = target.start()
    target_end = target.end()
            
    for range_start, range_end in spoiler_ranges:
        if target_start <= range_end and range_start < target_end:
            result.add(target_name)
            
print(result)
print("-----------------------------------------------------------")