import string

def solution(s, skip, index):
    answer = ''
    skip = set(skip)
    lower_alphabet = [
        char
        for char in string.ascii_lowercase
        if char not in skip
    ]
    print(lower_alphabet)
    
    # 처음 작성한 코드
    # for char in list(s):
    #     char_index = lower_alphabet.index(char) + index
    #     if char_index >= len(lower_alphabet): 
    #         char_index -= len(lower_alphabet)
    #     answer += lower_alphabet[char_index]
    alphabet_encode = {
        char: lower_alphabet[(position + index) % len(lower_alphabet)]
        for position, char in enumerate(lower_alphabet)
    }
    
    answer = "".join(alphabet_encode[char] for char in s)
    
    return answer

if __name__ == "__main__":
    
    s ="aukks"
    skip = "wbqd"	
    index = 5
    print(solution(s,skip,index))
    pass