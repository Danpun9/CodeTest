import math

def solution(signals):
    # 최소공배수
    lcm_period = 1
    for G, Y, R in signals:
        P = G + Y + R
        lcm_period = math.lcm(lcm_period, P)
    
    G0, Y0, R0 = signals[0]
    P0 = G0 + Y0 + R0
    
    # 첫 신호등이 노란불이 되는 주기를 기준으로 탐색
    for base in range(0, lcm_period, P0):
        for offset in range(G0 + 1, G0 + Y0 + 1):
            t = base + offset
            
            # 나머지 신호등들도 모두 노란불인지 확인
            all_yellow = True
            for i in range(1, len(signals)):
                G, Y, R = signals[i]
                P = G + Y + R
                rem = (t - 1) % P
                if not (G <= rem < G + Y):
                    all_yellow = False
                    break
            
            if all_yellow:
                return t
                
    return -1