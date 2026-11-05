def solution(k, m, score):
    answer = 0
    score_iter = iter(sorted(score, reverse=True))
    
    '''
    iter의 next를 활용하는 방법
    *[score_iter] => (1,2,3,...) * m => (1,2,3,...) (1,2,3,...) (1,2,3,...)
    이 때 score_iter 이터레이터 3개 복사가 아니라 
    같은 이터레이터 객체에 대한 참조를 3개 담은 리스트를 만든다
    * 참조의 반복, 순회 상태 공유
    '''
    for s in zip(*[score_iter] * m):
        answer += min(s) * m
    
    return answer

if __name__ == "__main__":
    k = 4
    m = 3
    score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
    print(solution(k, m, score))
    a = [[]] * 3
    a[1].append(3)
    a[0].append(4)
    print(a)
    pass