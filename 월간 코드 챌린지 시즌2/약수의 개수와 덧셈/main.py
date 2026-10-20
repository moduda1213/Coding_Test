'''
start : 16:05
end : 16:40
'''
from math import isqrt

def solution(left, right):
    
    answer = 0
    # case 1
    # scope = set(range(left, right+1))
    # result = {
    #     number: sum(number % n == 0 for n in range(1,number+1))
    #     for number in scope
    # }
    # print(result)
    # answer = sum(key if value % 2 == 0 else key*-1 for key, value in result.items())
        
    # case 2
    # 완전제곱수 n^2 = n *n 나타낼 수 있는 수 (0,1,4,9,16....)
    # -> 완전제곱수의 약수는 항상 홀수
    # 제곱근(루트) = isqrt(4) -> 2
    
    answer = sum(
    -number if isqrt(number) ** 2 == number else number
    for number in range(left, right+1)
    )
    return answer

if __name__ == "__main__":
    left = 24
    right = 27
    print(solution(left, right))
    pass