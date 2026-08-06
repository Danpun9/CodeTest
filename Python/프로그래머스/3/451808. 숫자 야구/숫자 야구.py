# 스트라이크/볼 판정
def get_sb(origin, test):
    a = []
    a.append(origin // 1000 % 10)
    a.append(origin // 100  % 10)
    a.append(origin // 10   % 10)
    a.append(origin // 1    % 10)
    b = []
    b.append(test // 1000 % 10)
    b.append(test // 100  % 10)
    b.append(test // 10   % 10)
    b.append(test // 1    % 10)

    s = set(a)
    strike = 0
    ball = 0

    for i in range(0,4):
        if a[i] == b[i]:
            strike += 1
        elif b[i] in s:
            ball += 1
    
    return f"{strike}S {ball}B"
    

def solution(n, submit):
    all_pool = []

    for i in range(1234, 9876+1):
        n1 = i // 1000 % 10
        n2 = i // 100  % 10
        n3 = i // 10   % 10
        n4 = i // 1    % 10
        
        if n1==0 or n2==0 or n3==0 or n4==0: continue
        if n1==n2 or n1==n3 or n1==n4: continue
        if n2==n3 or n2==n4: continue
        if n3==n4: continue
        all_pool.append(i)

    pool = list(all_pool)
    while (True):
        if len(pool) == 1:
            return pool[0]
        if len(pool) == len(all_pool):
            best_guess = pool[0]
        else:
            best_guess = None
            min_max_size = float("inf")

            # 미니맥스
            for g in all_pool:
                hint_cnts = {}

                for target in pool:
                    h = get_sb(g, target)
                    hint_cnts[h] = hint_cnts.get(h,0) + 1

                max_size = max(hint_cnts.values())

                if max_size < min_max_size:
                    min_max_size = max_size
                    best_guess = g

                elif max_size == min_max_size:
                    if g in pool and best_guess not in pool:
                        best_guess = g

        hint = submit(best_guess)
        if hint == "4S 0B":
            return best_guess

        # guess 숫자와 기존 pool 내부의 숫자를 비교하여 submit 결과와 같은 숫자만 남기기
        pool = [i for i in pool if get_sb(best_guess, i) == hint]
    
