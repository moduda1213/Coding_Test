from itertools import combinations

def solution(number):
    answer = 0
    
    # case1
    # combinations
    for i, j, k in combinations(range(len(number)), 3):
        if number[i] + number[j] + number[k] == 0:
            answer += 1
    
    # case2
    # combinations 사용 불가하다면
    n = len(number)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    
    
    return answer

if __name__ == "__main__":
    number = [-1, 1, -1, 1]
    print(solution(number))
    pass