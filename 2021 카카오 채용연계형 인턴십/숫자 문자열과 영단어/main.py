'''
start : 15:42
end : 15:55
'''
def solution(s):
    numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    
    # case 1
    # import re
    # for idx, number in enumerate(numbers):
    #     s = re.sub(number, str(idx), s)
        
    # return int(s)

    # case 2
    for digit, number in enumerate(numbers):
        s = s.replace(number, str(digit))
    
    return int(s)

if __name__ == "__main__":
    s = "one4seveneight"
    print(solution(s))
    pass