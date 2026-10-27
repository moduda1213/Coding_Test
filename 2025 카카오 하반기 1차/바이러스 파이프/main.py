'''
dfs(0, 0, {6})
  A 선택 → spread → {4, 5, 6}
  dfs(1, A, {4, 5, 6})
    B 선택 → spread → {3, 4, 5, 6, 7}
    dfs(2, B, {3, 4, 5, 6, 7})
      C 선택 → spread → {1, 2, 3, 4, 5, 6, 7}
      dfs(3, C, {1, 2, 3, 4, 5, 6, 7})
        answer = 7
'''

def solution(n, infection, edges, k):
    graph = [[] for _ in range(n + 1)]
    
    for x, y, pipe in edges:
        graph[x].append((y, pipe))
        graph[y].append((x, pipe))
    
    # kind 종류의 파이프를 한 번 열었을 때 감염되는 전체 노드
    def spread(infected, pipe):
        reached = infected.copy()
        stack = list(infected)
        
        while stack:
            current = stack.pop()
            
            for neighbor, edge_pipe in graph[current]:
                if edge_pipe == pipe and neighbor not in reached:
                    reached.add(neighbor)
                    stack.append(neighbor)
                    
        return reached
    
    answer = 1
    
    def dfs(depth, previous_pipe, infected):
        nonlocal answer
        
        answer = max(answer, len(infected))
        
        if depth == k or answer == n:
            return
        
        for pipe in (1,2,3):
            # 같은 종류를 연속해서 열어도 감염 상태가 변하지 않음
            if pipe == previous_pipe:
                continue
            
            next_infected = spread(infected, pipe)
            
            # 새 감염이 없다면 이 행동을 쓸 이유가 없음
            if len(next_infected) > len(infected):
                dfs(depth+1, pipe, next_infected)
            
    dfs(0,0,{infection})
    return answer

if __name__ == "__main__":
    n = 7
    infection = 6
    edges = [[1, 2, 3], [1, 4, 3], [4, 5, 1], [5, 6, 1], [3, 6, 2], [3, 7, 2]]
    k = 3
    print(solution(n, infection, edges, k))
    pass