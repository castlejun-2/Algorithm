from sys import stdin
dx=[0,0,-1,1]
dy=[1,-1,0,0]

result_max=0

def back_tracking(x,y,arr):
    global result_max
    result_max=max(len(arr),result_max)
    for i in range(4):  #상하좌우로 탐색
        a=x+dx[i] 
        b=y+dy[i]
        if 0<=a<R and 0<=b<C and not visited[ord(alpha_list[a][b])-65]: #(a,b)가 범위내에 존재하고, 아직 방문하지 않은 알파벳이라면
            visited[ord(alpha_list[a][b])-65]=1 #해당 알파벳의 방문을 확인하여 주고,
            arr.append(alpha_list[a][b])  #해당 값을 list에 추가해 준 후
            back_tracking(a,b,arr)  #다시 백트래킹을 통해 뒤의 값들을 이어나간다.
            visited[ord(alpha_list[a][b])-65]=0 #탐색이 끝나면 다음 반복을 위해 해당 알파벳의 방문을 취소하여주고,
            arr.pop() #리스트에 붙혀준 값또한 방문을 취소했으므로 빼준다.
    
R,C=map(int,stdin.readline().split())
alpha_list=[list(map(str,stdin.readline().strip())) for _ in range(R)]
visited=[0]*26  #set()보다 list가 해당 문제에서 더 빠른 속도를 보여 각 알파벳의 방문 여부를 나타내는 list 생성
visited[ord(alpha_list[0][0])-65]=1
back_tracking(0,0,[alpha_list[0][0]])
print(result_max)
