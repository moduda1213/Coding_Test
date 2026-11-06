def solution(food):
    answer = ''
    
    dstb = [f // 2 for f in food]
    
    table = ''.join([str(idx) * amount for idx, amount in enumerate(dstb) if amount > 0])
    answer = table + '0' + table[::-1]
    return answer

if __name__ == "__main__":
    food= [1, 7, 1, 2]
    print(solution(food))
    print('f'*3)
    pass