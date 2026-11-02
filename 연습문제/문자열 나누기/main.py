def solution(s):
    answer = 0
    
    # # 같고 다른 문자를 카운팅
    # target = ''
    # same = diff = 0
    
    # for char in s:
    #     if same == 0:
    #         target = char
        
    #     if char == target:
    #         same += 1
    #     else:
    #         diff += 1
        
    #     if same == diff:
    #         answer += 1
    #         same = diff = 0
    
    # # 더 이상 읽을 문자가 없는 경우를 위해
    # if same:
    #     answer += 1
    
    # 차이 하나만 세는 방법
    balance = 0
    target = ''
    
    for char in s:
        if balance == 0:
            target = char
        
        balance += 1 if char == target else -1
    
        if balance == 0:
            answer += 1
    
    if balance > 0:
        answer += 1
        
    return answer

if __name__ == "__main__":
    s = "banana"
    print(solution(s))
    pass