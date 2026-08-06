import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))

    # dp[i][j]: i번째 카드부터 j번째 카드까지 남았을 때 최대 점수
    dp = [[0] * n for _ in range(n)]

    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1

            if (n - l) % 2 == 0:  # 근우 턴
                if i == j:
                    dp[i][j] = cards[i]
                else:
                    dp[i][j] = max(
                        cards[i] + dp[i + 1][j], cards[j] + dp[i][j - 1]
                    )  # 근우 턴에는 근우가 얻을 점수 최대화
            else:  # 명우 턴
                if i == j:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(
                        dp[i + 1][j], dp[i][j - 1]
                    )  # 명우 턴에는 근우가 얻을 점수를 최소화(명우가 최대화)

    print(dp[0][n - 1])
