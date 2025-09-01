import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        ci, ki = input().split()
        ki = int(ki)
        arr.append([ci, ki])

    word = ''
    for i in range(N):
        word += arr[i][0] * arr[i][1]

    print(f'#{tc}')

    for i in range(len(word)//10):
        print(word[10*i:10*(i+1)])

    print(word[len(word) - (len(word)%10):])