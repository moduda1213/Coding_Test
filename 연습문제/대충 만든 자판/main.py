def solution(keymap, targets):
    answer = []
    
    min_press = {}
    for key in keymap:
        for press_count, char in enumerate(key, start=1):
            if char not in min_press:
                min_press[char] = press_count
            else:
                min_press[char] = min(
                    min_press[char],
                    press_count
                )
                
    print(min_press)
    
    for target in targets:
        total = 0
        for char in target:
            if char not in min_press:
                total = -1
                break
            else:
                total += min_press[char]
        answer.append(total)
    
    return answer

if __name__ == "__main__":
    a = solution(["ABACD", "BCEFD"],["ABCD","AABB"])

    """
    - `keymap`의 각 원소가 하나의 키라는 점
    - 문자열 내부 인덱스가 누르는 횟수와 연결된다는 점
    - 같은 문자에 대해 모든 문자열 중 최소 위치를 찾아야 한다는 점
    - 대상 문자열은 문자별 최소 비용의 합으로 계산한다는 점
    """