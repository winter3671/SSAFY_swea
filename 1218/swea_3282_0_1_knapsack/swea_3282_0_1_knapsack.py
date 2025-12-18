'''
1. 문제 분석
가방의 물건들 중 몇개를 골라 K 이하의 부피로 가장 큰 가치를 담아야 한다.

2. 풀이 방법 고안
대표적인 DP문제이다.
최대치를 찾아야하기 때문에 역순으로 탐색해야 한다.
'''
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    value_and_cost = []
    for _ in range(N):
        V, C = map(int, input().split())
        value_and_cost.append((V, C))

    dp = [0] * (K + 1)

    for value, cost in value_and_cost:
        for i in range(K, value - 1, -1):
            dp[i] = max(dp[i], dp[i - value] + cost)

    print(f'#{tc} {dp[K]}')