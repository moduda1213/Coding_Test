def solution(t, p):
    answer = 0
    length = len(p)
    
    answer = sum(
        t[i:i+length] <= p
        for i in range(len(t) - length + 1 )
    )
    
    # digit = len(p)
    # length = len(t)
    # for num in range(length - digit + 1 ):
    #     print(t[num:num+digit])
    #     if int(t[num:num+digit]) <= int(p): answer+=1
    return answer

if __name__ == "__main__":
    t = "3141592"
    p = "271"
    print(solution(t, p))
    
    print(sum([True, False, True]))
    pass