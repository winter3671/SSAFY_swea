'''
1. 문제 분석
M X M의 파리채를 한번 내리쳐서 최대한 많은 파리를 죽일 때, 죽은 파리의 개수를 구하시오

2. 풀이 방법 고안
N은 15이하이므로, 이중for문을 돌면서 구현하면 될 것 같다.
'''
import sys
sys.stdin = open('input (1).txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_area = 0
            for k in range(i, i + M):
                for l in range(j, j + M):
                    sum_area += arr[k][l]
            max_num = max(max_num, sum_area)

    print(f'#{tc} {max_num}')