'''
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,
'''
def solution(answers):
    result = []
    supozas = [[1,2,3,4,5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [0,0,0]
    
    for i, correct in enumerate(answers):
        for person in range(3):
            supoza = supozas[person]
            if correct == supoza[i % len(supoza)]:
                scores[person] += 1
    
    highest = max(scores)
    return [person + 1 for person, score in enumerate(scores)
            if score == highest]
    

if __name__ == "__main__":
    answers = [1,2,3,4,5]
    print(solution(answers))
    pass