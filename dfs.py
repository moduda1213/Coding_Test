graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

# 구현방법 1 : 재귀함수
# 나를 다시 호출하면서 깊게 들어가는 방식
def dfs_recursive(node, visited=[]):
    # 현재 노드를 방문처리
    visited.append(node)
    
    # 현재 노드와 연결된 다른 노드 확인
    for neighbor in graph[node]:
        # 아직 방문하지 않았다면
        if neighbor not in visited:
            # 그곳으로 들어가 다시 탐색 시작(재귀 호출)
            dfs_recursive(neighbor, visited)
            
    return visited

# 구현방법 2 : 스택 자료구조
# while 사용, LIFO(LAST-IN-FIRST-OUT)
def dfs_stack(start_node):
    visited = [] # 방문한 노드 목록
    stack = [start_node] # 방문할 노드 목록
    
    # stack 남는 것 없이 반복
    while stack:
        # 가장 뒤 꺼냄
        current = stack.pop()
        
        # 방문하지 않았다면
        if current not in visited:
            # 방문 처리
            visited.append(current)
            
        # 연결된 노드 스택에 추가 (Reverse 하는 이유는 꺼낼 때 순서 맞추기 위함, 필수는 아님)
        # 스택에 넣을 때 ['B', 'C'] 순으로 넣으면, 나중에 'C'가 먼저 꺼내짐.
        # 알파벳 순서 탐색을 원하면 graph[current]를 역순으로 넣거나 그대로 넣어서 순서 조절 가능
        for neighbor in reversed(graph[current]):
            if neighbor not in visited:
                stack.append(neighbor)
                        
    return visited
        
if __name__ == "__main__" :
    print(dfs_stack('A'))
    
