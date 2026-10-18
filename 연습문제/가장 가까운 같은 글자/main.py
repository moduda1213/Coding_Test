def solution(s):
    answer = []
    
    # 첫번째 풀이
    # temp = {}
    # s_list = list(s)
    
    # for index, char in enumerate(s_list):
    #     if char not in temp:
    #         temp[char] = index
    #         answer.append(-1)
    #     else:
    #         answer.append(index - temp[char])
    #         temp[char] = index
            
    # print(temp)
    
    temp = {}
    s_list = list(s)
    for index, char in enumerate(s_list):
        prev = temp.get(char)
        
        answer.append(
            -1 if prev is None else index - prev
        )
        temp[char] = index    
    
    return answer

if __name__ == "__main__":
    s = "foobar"
    a = {}
    print(solution(s))
    pass