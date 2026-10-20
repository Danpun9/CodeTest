def solution(grid):
    n, m = len(grid), len(grid[0])
    
    # 오른쪽(0), 왼쪽(1), 아래(2), 위(3)
    RIGHT, LEFT, DOWN, UP = 0, 1, 2, 3
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    
    # 현재 진행 방향(direction)으로 칸에 진입할 때, 해당 칸에 유효한 선로 목록
    placeable = {
        RIGHT: [1, 3, 4, 7],
        LEFT:  [1, 3, 5, 6],
        DOWN:  [2, 3, 4, 5],
        UP:    [2, 3, 6, 7],
    }
    
    visited = [[0] * m for _ in range(n)]
    answer = 0

    # 현재 위치(y, x)의 선로를 통과한 후의 다음 좌표와 진행 방향 반환
    def next_state(y, x, direction):
        rail = grid[y][x]
        if rail == 4: # 좌상
            direction = LEFT if direction == DOWN else UP
        elif rail == 5: # 우상
            direction = RIGHT if direction == DOWN else UP
        elif rail == 6: # 우하
            direction = RIGHT if direction == UP else DOWN
        elif rail == 7: # 좌하
            direction = LEFT if direction == UP else DOWN
        
        # 방향 유지
        return y + dy[direction], x + dx[direction], direction

    # 격자 내의 모든 선로가 조건에 맞게 방문되었는지 확인
    def visited_all_rails():
        for y in range(n):
            for x in range(m):
                if 1 <= grid[y][x] <= 7:
                    if grid[y][x] == 3:
                        if visited[y][x] != 2:  # 3번 십자 선로는 2번 방문
                            return False
                    else:
                        if visited[y][x] != 1:  # 나머지 선로는 1번 방문
                            return False
        return True

    def dfs(y, x, direction):
        nonlocal answer
        
        # 격자 범위 밖, 장애물
        if not (0 <= y < n and 0 <= x < m) or grid[y][x] == -1:
            return
        
        # 이미 선로가 있는 칸인데, 현재 진행 방향으로 진입할 수 없는 선로
        if grid[y][x] != 0 and grid[y][x] not in placeable[direction]:
            return
            
        # 방문 횟수 초과
        if grid[y][x] == 3 and visited[y][x] == 2:
            return
        if grid[y][x] != 0 and grid[y][x] != 3 and visited[y][x] == 1:
            return

        # 현재 칸 방문
        visited[y][x] += 1

        # 도착점 (n-1, m-1)에 도달한 경우
        if y == n - 1 and x == m - 1:
            # 도착점의 선로(1 또는 2)를 끝까지 통과한 후 밖으로 나가는 방향이 맞는지,
            # 그리고 모든 선로를 조건에 맞게 방문했는지 확인
            if visited_all_rails():
                answer += 1
            visited[y][x] -= 1
            return

        # 현재 칸이 빈칸인 경우: 진입 가능한 선로를 하나씩 설치
        if grid[y][x] == 0:
            for rail in placeable[direction]:
                grid[y][x] = rail
                ny, nx, nd = next_state(y, x, direction)
                dfs(ny, nx, nd)
                grid[y][x] = 0
                
        # 선로가 놓여 있는 칸인 경우: 해당 선로를 따라 다음 칸으로 이동
        else:
            ny, nx, nd = next_state(y, x, direction)
            dfs(ny, nx, nd)

            
        visited[y][x] -= 1

    # 시작점 (0, 0)은 항상 1번 선로
    visited[0][0] = 1
    dfs(0, 1, RIGHT)
    
    return answer