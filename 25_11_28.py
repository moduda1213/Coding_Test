def find_string(n):
    length = 1
    total = 0
    while total + 26**length < n:
        total += 26**length
        length += 1
        
    pos = n - total - 1
    result = []
    for _ in range(length):
        result.append(chr(ord('a') + pos % 26))
        pos //= 26
    
    return ''.join(reversed(result))

def find_position(s):
    """문자열 s의 위치를 반환"""
    length = len(s)
    total_before = sum(26**i for i in range(1, length))
    
    position = 0
    for i, char in enumerate(s):
        char_index = ord(char) - ord('a') # ord : 유니코드
        position += char_index * (26 ** (length - 1 - i))
    
    return total_before + position + 1

def solution(n, bans):
    # 1. 금지된 문자열들의 위치를 구해서 정렬
    ban_positions = sorted([find_position(ban) for ban in bans])
    
    # 2. n번째를 찾되, 금지된 위치를 건너뛰기
    target = n
    for ban_pos in ban_positions:
        if ban_pos <= target:
            target += 1
        else:
            break
    
    # 3. 최종 위치의 문자열 반환
    return find_string(target)

solution(7388, ["gqk", "kdn", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"])
