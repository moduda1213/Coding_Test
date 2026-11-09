import re
def solution(ingredient):
    answer = 0
    # ingredient = list(map(str, ingredient))
    stack = []
    
    for char in ingredient:
        stack.append(char)
        
        #if len(stack) >= 4 and stack[-4:] == list('1231'):
        if len(stack) >= 4 and stack[-4:] == [1,2,3,1]:
            del stack[-4:]
            answer += 1
            
    return answer

if __name__ == "__main__":
    ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
    print(solution(ingredient))
    pass