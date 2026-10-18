import re

def solution(wallpaper):
    
    # 내가 작성한 코드 ###
    # [처음 #을 갖고 있는 배열 idx, x축이 가장 작은 # 위치, 배열길이, y축이 가장 큰 # 위치]
    # result = [None, None, None, None]
    # for idx, area in enumerate(wallpaper):
    #     for match in re.finditer(r"#", area):
    #         if result[0] is None or result[0] > idx:
    #             result[0] = idx
                
    #         if result[1] is None or result[1] > match.start():
    #             result[1] = match.start()
                
    #         result[2] = len(wallpaper)
            
    #         if result[3] is None or result[3] < match.end():
    #             result[3] = match.end()
    # print(result)
    
    files = [
        (row, col)
        for row, line in enumerate(wallpaper) 
        for col, cell in enumerate(line)
        if cell == "#"
    ]
    
    print(files)
    # `*`(아스타리스크) 는 리스트의 요소들을 *함수의 개별 인자로 펼치는 연산자(argument unpacking)**
    rows, cols = zip(*files) 
    print(rows, cols)
    return [
        min(rows),
        min(cols),
        max(rows) + 1,
        max(cols) + 1
    ]
    
    
if __name__ == "__main__":
    wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
    result = solution(wallpaper)
    print(result)