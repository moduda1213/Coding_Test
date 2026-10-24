'''
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,
'''
def solution(answer):
    
    len = 10000
    lps = [0] * len
    j = 0
    
    for i in range(1, len):
        while j > 0 and answer[i] != answer[j]:
            j = lps[j - 1]
            
        if answer[i] == answer[j]:
            j += 1
            lps[i] = j
    
    size = len - lps[-1]
    if size * 2 <= len:
        return answer[:size]
    

if __name__ == "__main__":
    answer = [1,2,3,4,5] * (10000 // 5)
    print(solution(answer))
    pass