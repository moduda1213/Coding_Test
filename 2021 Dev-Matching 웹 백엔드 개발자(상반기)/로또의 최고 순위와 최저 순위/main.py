def solution(lottos, win_nums):
    answer = []
    
    # case 1
    # 이중 for문 => O(n x m)
    # min = sum(lotto == win_num for lotto in lottos for win_num in win_nums)
    # print(min)
    # max = sum(lotto == 0 for lotto in lottos) + min
    # print(max)
    
    # min_rate = 7 - min if min > 1 else 6
    # max_rate = 7 - max if max > 1 else 6
    # print(max_rate, min_rate)
    
    # case 2
    # list -> 앞에서부터 찾으므로 O(n)
    # set -> 집합. O(1)
    winnging = set(win_nums)
    matchs = sum(lotto in winnging for lotto in lottos)
    unknown = lottos.count(0)
    ranks = [6,6,5,4,3,2,1]
    
    result = [ranks[matchs + unknown], ranks[matchs]]
    print(result)
    return answer

if __name__ == "__main__":
    lottos = [0, 0, 0, 0, 0, 0]
    win_nums = [38, 19, 20, 40, 15, 25]
    print(solution(lottos, win_nums))
    pass