def solution(a, b):
    answer = 1234567890
    print(sum(x*y for x,y in zip(a,b)))
    return answer

if __name__ == "__main__":
    a = [-1,0,1]
    b =[1,0,-1]
    print(solution(a,b))
    pass