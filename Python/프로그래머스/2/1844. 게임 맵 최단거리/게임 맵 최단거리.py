from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 1
    
    queue = deque([(0, 0)])
    
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
    
    return dist[n-1][m-1]