from sys import stdin

N,M=map(int,stdin.readline().split())
NM_list=list(map(int,stdin.readline().split()))

NM_list.sort()

def bfs(arr,idx):
    if(len(arr)==M):
        print(' '.join(map(str,arr))) #list의 길이가 M이 되면 하나씩 꺼내 공백을 기준으로 출력
    else:
        for i in range(N):
            if NM_list[i] not in arr: #자신을 제외하고, 오름차순으로 출력 될 수 있도록 앞의 index부터 append
                arr.append(NM_list[i])  
                bfs(arr,i+1)
                arr.pop() #bfs를 통해 탐색이 끝나면, 방금 삽입하였던 값은 pop
bfs([],0)
