def solution(sizes):
    # 모든 수 중 가장 큰 수
    # 모든 수 / 2 => 가장 큰 수
    
    # case 1
    # 다 펼치고 큰 값과 중간값(size(len)-1)을 구하는 방식
    # 하지만 이렇게 하면 케이스의 가로*세로 관계를 잃어버림
    # sizes = sorted(s for size in sizes for s in size)
    # size_len = len(sizes)
    # w = sizes[-1]
    # h = sizes[size_len//2 - 1]
    
    # case 2
    # 1.큰 값 중들 가장 큰 값
    # 2.작은 값들 중 가장 큰 값
    # 1,2를 구하면 내가 구상했던 것과 일치하면서 가로*세로 관계도 지킬 수 있음
    w = max(max(size) for size in sizes)
    h = max(min(size) for size in sizes)
    
    return w*h

if __name__ == "__main__":
    sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
    print(solution(sizes))
    pass