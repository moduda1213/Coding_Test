def solution(n, m, section):
    answer = 0
    painted_section = 0
    
    for s in section:
        if s > painted_section:
            answer += 1
            painted_section = s + m - 1
            
    return answer

if __name__ == "__main__":
    print(solution(5,4,[1, 3]))