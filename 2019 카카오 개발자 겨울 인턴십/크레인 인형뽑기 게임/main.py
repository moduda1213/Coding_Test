def solution(board, moves):
    answer = 0
    box = []
    # 시계 90 돌려 아래에서 위로 재정렬
    # bottomUp = [...] 파이썬 관례상  bottomUp => bottom_up
    bottom_up = [
            [x for x in row if x != 0]
            for row in zip(*board[::-1])
        ]
    print(bottom_up)
    
    for move in moves:
        # sum을 매번 돌리면 최대 O(nm)
        # if sum(bottom_up[move-1]) == 0 : continue
        
        column = bottom_up[move-1]
                
        if not column : continue
        
        pick = column.pop()
        if box and pick == box[-1]:
            box.pop()
            answer += 2
        else:
            box.append(pick)
    
    print(box)
    return answer

if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves =	[1,5,3,5,1,2,1,4]
    
    print(solution(board, moves))
    pass