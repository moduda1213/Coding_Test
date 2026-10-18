'''
1. 모든 가능한 주사위 조합 생성
2. 각 조합의 합 분포 계산 (동적 프로그래밍 방식)
3. 모든 조합 쌍에 대해 승리 횟수 계산
4. 가장 많이 이기는 조합 선택
문제 : https://school.programmers.co.kr/learn/courses/30/lessons/258709
참고 : https://github.com/skysign/WSAPT/blob/master/2024%20KAKAO%20WINTER%20INTERNSHIP%20%EC%A3%BC%EC%82%AC%EC%9C%84%20%EA%B3%A0%EB%A5%B4%EA%B8%B0/main.py
'''

from itertools import combinations

def solution(dices):
    answer = []
    combs: dict = {}
    
    dice_indexes = [i for i in range(len(dices))]
    
    dice_combs = combinations(dice_indexes, len(dices)//2)
    dice_combs = list(dice_combs)
    
    for dice_comb in dice_combs:
        # 선택된 주사위의 모든 경우의 수를 찾고,
        all_dice_combs = get_all_combs_of_dices(dices, dice_comb)
        combs[tuple(dice_comb)] = all_dice_combs
    
    max_wins = 0
    
    for dice_comb in dice_combs:
        A_dices = dice_comb
        B_dices = tuple(set(dice_indexes).difference(A_dices))
        
        new_A_wins = get_wins(combs[A_dices], combs[B_dices])
        
        if new_A_wins > max_wins:
            max_wins = new_A_wins
            answer = list(A_dices)
            
    answer = list(map(lambda x:x+1, answer))
    return answer        
        
def get_all_combs_of_dices(dices: list[int], dice_comb: list[list[int]]):
    inputs : dict = {}
    inputs[0] = 1
    outputs: dict = {}
    
    for dice_index in dice_comb:
        dice = dices[dice_index]
        
        for number in inputs.keys():
            for dice_number in dice:
                key = number + dice_number
                
                if key in outputs.keys():
                    outputs[key] += inputs[number]
                else:
                    outputs[key] = inputs[number]
        inputs = outputs
        outputs = {}
    return inputs

# 각 주사위 조합의 모든 경우의 수를 서로 비교, 이기는 수를 세어본다
def get_wins(A_dice_all_combs: dict, B_dice_all_combs: dict) -> int:
    rtn = 0
    
    for a_number in A_dice_all_combs.keys():
        print(A_dice_all_combs.keys())
        for b_number in B_dice_all_combs.keys():
            print(B_dice_all_combs.keys())
            if a_number > b_number:
                rtn += (A_dice_all_combs[a_number] * B_dice_all_combs[b_number])
    
    return rtn

solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]])
    