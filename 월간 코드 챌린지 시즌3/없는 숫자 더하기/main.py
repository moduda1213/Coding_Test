'''
start : 20:25
중복되지 않은 숫자 리스트인 점
0~9까지 합 - numbers 합 => [numbers] 없는 숫자들의 합
end : 20:37
'''
def solution(numbers):
    # 1. case 1
    all_num = sum(range(0,10))
    return all_num - sum(numbers)


if __name__ == "__main__":
    numbers = 5,8,4,0,6,7,9
    print(solution(numbers))
    pass