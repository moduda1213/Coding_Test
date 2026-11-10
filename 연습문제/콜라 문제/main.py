def solution(a, b, n):
    answer = 0
    
    # case 1
    # n//a * b는 교환한 콜라 개수
    while True:
        if n//a  > 0:
            answer += n//a * b
            n = (n//a * b) + n%a
        
        if n // a == 0:
            break
    
    # case 2
    # divmod
    while n >= a:
        exchanges, remainder = divmod(n, a)
        received = exchanges * b
        
        answer += received
        n = remainder + received
        
    # case 3
    # 전체 교환 횟수를 바로 계산
    if n < a:
        return 0
    
    exchanges = 1 + (n -a) // (a-b)
    return exchanges * b
    
    return answer

if __name__ == "__main__":
    a=3
    b=1
    n=20
    print(solution(a,b,n))
    pass