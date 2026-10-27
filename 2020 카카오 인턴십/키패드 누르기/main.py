def distance(a,b) :
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solution(numbers, hand):
    answer = []
    keypad = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ['*',0,'#']
    ]
    position = {}
    for row, line in enumerate(keypad):
        for col, value in enumerate(line):
            position[value] = (row, col)
    
    left_hand = position['*']
    right_hand = position['#']
    
    for number in numbers:
        press = position[number]
        
        if number in (1,4,7):
            chosen = 'L'
        elif number in (3,6,9):
            chosen = 'R'
        else:
            left_distance = distance(left_hand, press)
            right_distance = distance(right_hand, press)
            
            if left_distance < right_distance:
                chosen = 'L'
            elif left_distance > right_distance:
                chosen = 'R'
            else:
                chosen = hand[0].upper()
        
        # 파이썬 문자열은 수정할 수 없습니다
        # 문자열은 수정할 수 없으므로, 각 단계는 기존 내용과 새 글자를 합친 결과를 answer에 다시 할당하는 것과 같아
        # 1+2+3+4 ... => n(n+1)/2 최악의 경우 O(n^2) 시간복잡도를 가짐
        # answer += chosen
        answer.append(chosen)
        
        if chosen == 'L':
            left_hand = press
        else:
            right_hand = press
                
    return ''.join(answer)

if __name__ == "__main__":
    numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
    hand = 'right'
    print(solution(numbers, hand))
    pass