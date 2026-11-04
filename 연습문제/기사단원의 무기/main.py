from math import isqrt

def solution(number, limit, power):
    answer = 0
    
    '''
        약수는 곱이 n이 되는 쌍으로 나타난다
        i가 약수면 number // i 도 약수다
        ex) number = 16
        1, 16
        2, 8
        4, 4
    '''
    divisor = []
    for n in range(1,number + 1):
        count = 0
        for i in range(1, isqrt(n) + 1):
            if n % i == 0:
                count += 1 if i == n // i else 2

        divisor.append(count)
        
    answer = sum([power if divi > limit else divi for divi in divisor])
    
    # case 2
    # 각 수의 배수에 약수 개수를 1씩 더하는 방법
    counts = [0] * (number + 1)
    
    # divisor는 자신의 모든 배수의 약수라는 성질을 사용합니다.
    # 시간은 O(N log N), 공간은 O(N)
    for divisor in range(1, number+1):
        for multiple in range(divisor, number + 1, divisor):
            counts[multiple] += 1
    
    answer = sum([power if count > limit else count for count in counts[1:]])
    return answer

if __name__ == "__main__":
    number, limit, power = (10 , 3, 2)
    print(solution(number, limit, power))
    counts = [0] * (number + 1)

    for divisor in range(1, number + 1):
        print(f'divisor: {divisor}')
        for multiple in range(divisor, number + 1, divisor):
            print(f'divisor, number + 1, divisor: {divisor, number + 1, divisor} multiple: {multiple}')
            
            counts[multiple] += 1
            
    print(counts)
    pass