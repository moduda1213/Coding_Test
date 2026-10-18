# https://school.programmers.co.kr/learn/courses/30/lessons/178871?language=python3
# 코딩테스트 연습 > 연습문제 > 달리기 경주

# 데이터가 많아질수록 처리시간이 늘어나는 로직
'''
    전체 시간 복잡도 : O(M \times N)
        5 ≤ players의 길이 ≤ 50,000
        2 ≤ callings의 길이 ≤ 1,000,000
    최대로 50,000 * 1,000,000 초가 걸릴 수 있다
'''
def wrong_solution(players, callings):
    count = 0
    for idx, calling in enumerate(callings):
        if idx+1 <= len(callings)-1 and calling == callings[idx+1] :
            count+=1
            continue
        else :
            # 리스트의 길이에 비례 ==> 시간복잡도 O(N)
            cur = players.index(calling)
            switch = cur - count - 1

            # 제거 후 뒷부분 요소를 한 칸씩 당겨야 함 ==> 시간복잡도 O(N)
            players.pop(cur)
            
            # 삽입 후 뒷부분 요소를 한 칸씩 밀어야 함 ==> 시간복잡도 O(N)
            players.insert(switch, calling)

            count=0
    
    return players

# O(M \times N) ==> O(M+N) 전체 시간복잡도 개선
def correct_solution(players, callings):
    players_ranking = {player : i  for i,player in enumerate(players)}
    print(players_ranking)

    for calling in callings:
        current_rank = players_ranking[calling] # O(1)
        
        overtaking_rank = current_rank -1
        overtaken_player = players[overtaking_rank]

        # 파이썬 스와핑문법 사용  (a,b = b,a) ===> 시간복잡도 O(1)
        players[current_rank], players[overtaking_rank] = players[overtaking_rank], players[current_rank] 

        players_ranking[calling] = overtaking_rank
        players_ranking[overtaken_player] = current_rank

    print(players)
    print(players_ranking)

if __name__ == "__main__" : 
    players = ["mumu", "soe", "poe", "kai", "mine"]	
    callings = ["kai", "kai", "mine", "mine"]
    
    correct_solution(players, callings)
    