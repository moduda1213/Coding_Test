'''
1번 지표	라이언형(R), 튜브형(T)
2번 지표	콘형(C), 프로도형(F)
3번 지표	제이지형(J), 무지형(M)
4번 지표	어피치형(A), 네오형(N)

서로 점수 동일 or 점수 없을 경우 사전순
'''


def solution(survey, choices):
    answer = ''
    
    # case1
    # characteristic = ["RT", "CF", "JM", "AN"]
    # choice_type = {}
    # choices = [choice-4 for choice in choices]
    
    # for surv, choice in zip(survey, choices):
    #     if choice < 0:
    #         choice_type[surv[0]] = choice_type.get(surv[0], 0) + abs(choice)
    #     elif choice > 0:
    #         choice_type[surv[1]] = choice_type.get(surv[1], 0) + abs(choice)
            
    # for c in characteristic:
    #     op1 = choice_type.get(c[0],0)
    #     op2 = choice_type.get(c[1],0)
    #     if op1 < op2:
    #         answer += c[1]
    #     elif op1 == op2:
    #         answer += min(c[0], c[1])
    #     else:
    #         answer += c[0]
    # return answer
    
    # case 2
    # personality_types = ("RT", "CF", "JM", "AN")
    # scores = {}
    
    # for types, choice in zip(survey, choices):
    #     score = choice - 4
    #     if score < 0:
    #         personality_type = types[0]
    #         scores[personality_type] = scores.get(personality_type, 0) - score
    #     elif choice > 0:
    #         personality_type = types[1]
    #         scores[personality_type] = scores.get(personality_type, 0) + score
            
    # return "".join(
    #     max(types, key=lambda t: scores.get(t, 0))
    #     for types in personality_types
    # )
    
    # case 3
    scores = dict.fromkeys("RTCFJMAN", 0)
    personality_types = ("RT", "CF", "JM", "AN")
    
    for types, choice in zip(survey, choices):
        score = choice - 4
        if score < 0:
            scores[types[0]] += -score
        else:
            scores[types[1]] += score
    
    return "".join(
        max(sorted(types), key=scores.get)
        for types in personality_types
    )

if __name__ == "__main__":
    print(dict.fromkeys("RCJMATFN", 0))
    survey = ["AN", "CF", "MJ", "RT", "NA"]
    choices = [5, 3, 2, 7, 5]
    print(solution(survey, choices))
    pass