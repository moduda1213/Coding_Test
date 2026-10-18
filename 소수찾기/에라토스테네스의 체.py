'''
소수찾기
- 1~n 까지 숫자를 모두 나열한다.
- 1은 소수가 아니니 삭제
- 2의 배수를 모두 삭제한다.
- 3의 배수를 모두 삭제한다.
- 4의 배수를 모두 삭제 그러나 4의배수는 2의 배수이니 넘어간다.
- 5의 배수를 모두 삭제한다.
'''
from datetime import datetime
start_time = datetime.now()
print(f"start_time: {start_time}")

n=50000
num = set(range(2, n+1))

for i in range(2,n+1):
    if i in num:
        num -= set(range(2*i, n+1, i)) # range(start, end, step)
    
        
end_time = datetime.now()
print(f"end_time: {end_time}")
print(f"result: {num}")