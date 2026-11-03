import heapq

def solution(k, score):
    answer = []
    honor = []
    
    # 리스트 버전
    for s in score:
        #  key를 쓰면 min()이 반환하는 것은 비교에 사용한 숫자가 아니라, 원래 항목이라는 점
        if honor: 
            idx, min_score = min(enumerate(honor), key=lambda x: x[1])
            
        honor.append(s)
        if len(honor) > k and min_score < s:
            honor.pop(idx)
        if len(honor) > k:
            honor.pop()
        answer.append(min(honor))
        
    # case 2 . heapq
    # 가장 작은 값을 빠르게 꺼내기 위한 파이썬 표준 라이브러리
    # 기존 리스트를 최소 힙(min heap)으로 관리
    for s in score:
        if len(honor) < k:
            heapq.heappush(honor, s)
        else:
            heapq.heappushpop(honor, s)
        answer.append(min(honor))
    
    return answer

if __name__ == "__main__":
    k = 4
    score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
    print(solution(k, score))
    pass