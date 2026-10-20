def solution(absolutes, signs):
    answer = 123456789
    
    re = sum(value if sign else -value for value, sign in zip(absolutes, signs))
    print(re)
    return answer

if __name__ == "__main__":
    absolutes = [1,2,3]
    signs = [False,False,True]
    print(solution(absolutes, signs))
    pass