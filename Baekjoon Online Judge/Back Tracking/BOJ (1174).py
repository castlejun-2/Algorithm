N=int(input())

def dfs(num):
    answer.append(int(num))
    for k in range(0,int(num[-1])): #자신보다 작은 값들만 뒤에 붙혀나간다.
        dfs(num+str(k))
if N>1023:  #십진법으로 나타낼 수 있는 최대수의 index 가 1023
    print(-1)
else:
    answer=[]
    for i in range(10): #앞자리가 0~9로 시작하는 수를 찾는다
        dfs(str(i))
    print(sorted(answer)[N-1])