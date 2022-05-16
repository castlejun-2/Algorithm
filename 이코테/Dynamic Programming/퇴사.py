# DFS로 푼 문제 풀이
# N=int(input())
# consulting=[]
# answer=0

# def dfs(cnt,i):
#     global answer
#     for k in range(i,N):
#         if consulting[k][0]+k <=N:
#             answer=max(dfs(cnt+consulting[k][1],consulting[k][0]+k),answer)
#     return cnt
    
# for i in range(N):
#     T,P=map(int,input().strip().split())
#     consulting.append([T,P])

# dfs(0,0)
# print(answer)
N=int(input())
consulting=[]
dp=[0]*(N+1)
answer=0

for i in range(N):
    T,P=map(int,input().strip().split())
    consulting.append([T,P])
    
for i in range(N-1,-1,-1):
    time=consulting[i][0]+i #상담을 완료 후 종료일
    if time<=N: #만약 상담이 기간 내에 완료되는 경우
        dp[i]=max(consulting[i][1]+dp[time],answer) #현재 날짜의 상담을 통해 얻은 이익 + 상담 종료일 이후 얻는 최대이익 vs 현재 얻은 최대이익을 비교
        answer=dp[i]    #현재까지의 최댓값을 갱신
    else:
        dp[i]=answer    #상담이 기간 내에 종료되지 않는다면, 해당 일을 포함하지 않고 현재 날짜부터 마지막 날까지 얻는 최대이익을 현재 최댓값으로 반영

print(answer)