def solution(food):
    answer = ''
    
    # case1
    dstb = [f // 2 for f in food]
    
    table = ''.join([str(idx) * amount for idx, amount in enumerate(dstb) if amount > 0])
    answer = table + '0' + table[::-1]
    
    # case 2
    left = ''.join(
        str(i) * (amount//2)
        for i, amount in enumerate(food)
        if i > 0
    )
    
    return answer

if __name__ == "__main__":
    food= [1, 7, 1, 2]
    print(solution(food))
    print('f'*3)
    pass