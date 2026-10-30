from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    visited = [[False] * m for _ in range(n)]
    col_sum = [0] * m

    for r in range(n):
        for c in range(m):
            if land[r][c] == 1 and not visited[r][c]:
                visited[r][c] = True
                queue = deque([(r, c)])
                cnt = 0
                cols_spanned = set()
                
                while queue:
                    y, x = queue.popleft()
                    cnt += 1
                    cols_spanned.add(x)
                    
                    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < n and 0 <= nx < m:
                            if land[ny][nx] == 1 and not visited[ny][nx]:
                                visited[ny][nx] = True
                                queue.append((ny, nx))
                
                for col in cols_spanned:
                    col_sum[col] += cnt
    
    return max(col_sum)