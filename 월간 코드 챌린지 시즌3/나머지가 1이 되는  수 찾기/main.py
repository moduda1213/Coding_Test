from math import isqrt
def solution(n):
    
    # case1 : O(1000000)
    # for i in range(2,1000001):
    #     if n % i == 1:
    #         answer = i
    #         break
    
    # case 2 O(n)
    # return [i for i in range(2,n+1) if n % i ==1][0]
    
    # case3 : O(^n)
    target = n - 1
    # math.isqrt(n) : n 의 제곱근 
    for i in range(2, isqrt(target) + 1):
        if target % i == 0:
            return i
    return target # n-1이 소수일 경우
if __name__ == "__main__":
    
    n = 12
    print(solution(n))
    