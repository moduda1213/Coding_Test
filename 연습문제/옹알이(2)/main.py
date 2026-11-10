def solution(babbling):
    answer = 0
    talk_bab = ("aya", "ye", "woo", "ma")
    
    # case 1
    # 전체 입력 문자열 길이의 합을 S
    # 가장 긴 문자열 길이를 M
    # 시간 복잡도: O(S), 추가 공간: O(M) -> replace()가 새 문자열을 만둠
    for babb in babbling:
        
        # "yeye"는 같은 발음이 연속되므로 제외해야 하는데, replace()로는 모두 지워집니다.
        if any(tb * 2 in babb for tb in talk_bab):
            continue
        
        # "yayae"는 발음할 수 없지만, "aya"를 지우면 "ye"가 새로 만들어져 잘못 통과합니다.
        for tb in talk_bab:
            babb = babb.replace(tb, ' ')
        
        if not babb.strip(): 
            answer += 1    
            
    # case 2
    # index로 문자열을 읽으면서 현재 발음과 직전 발음을 비교
    # 시간 O(S), 공간복잡도: O(1)
    sounds = ("aya", "ye", "woo", "ma")

    for word in babbling:
        i = 0
        prev = ""

        while i < len(word):
            for sound in sounds:
                if word.startswith(sound, i) and sound != prev:
                    i += len(sound)
                    prev = sound
                    break
            else:
                # 일치하는 발음이 없거나 같은 발음이 연속된 경우
                break

        if i == len(word):
            answer += 1
    
    return answer

if __name__ == "__main__":
    babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
    print(solution(babbling))
    pass