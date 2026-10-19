'''
start: 20:44

10! = 10 * (10 + 1) / 2

end : 20:56
'''

def solution(price, money, count):
    # total = sum(
    #     price * c
    #     for c in range(1,count+1)
    # )
    
    # # case 1
    # return abs(money - total) if money - total < 0 else 0
    
    # case 2
    # return max(total - money, 0)

    # case 3
    # 10! = 10 * (10 + 1) / 2 (수열 합 공식)
    total = price * count * (count+1) // 2
    return max(total - money, 0)

if __name__ == "__main__":
    price = 3
    money = 20
    count = 4
    print(solution(price, money, count))
    pass