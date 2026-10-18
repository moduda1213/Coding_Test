"""
1. 범위를 벗어나는지
2. 장애물이 존재하는지
1,2 해당된다면 다음 명령으로 진행
"""
def solution(park, routes) -> list:
    height = len(park)
    width = len(park[0])
    direction = {
        "E" : (0, 1),
        "W" : (0, -1),
        "S" : (1, 0),
        "N" : (-1, 0)
    }
    
    # 시작 위치
    for row, line in enumerate(park):    
        col = line.find("S")
        if col != -1:
            current_row, current_col = row, col
            break
    
    # 이동
    for route in routes:
        way, distance = route.split(" ")
        distance = int(distance)
        dr, dc = direction[way]
        
        next_row, next_col = current_row, current_col
        can_move = True
        
        for _ in range(distance):
            next_row += dr
            next_col += dc
            print(next_row, next_col, width)
            # 범위가 벗어났는지
            if not(0 <= next_row < height and 0 <= next_col < width):
                can_move = False
                break
            
            # 장애물이 경로에 있는지
            if park[next_row][next_col] == "X":
                can_move = False
                break

        if can_move == True:
            current_row, current_col = next_row, next_col
    
    return [current_row, current_col]

if __name__ == "__main__":
    park = ["OSO","OOO","OXO","OOO"]	
    routes = ["E 2","S 3","W 1"]
    result = solution(park, routes)
    