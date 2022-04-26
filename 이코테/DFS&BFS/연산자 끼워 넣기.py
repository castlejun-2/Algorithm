import sys

def dfs(cnt,arr):
    global sum_min,sum_max,a_arr,add,sub,mul,div
    if cnt==N:  #연산자 사용 갯수가 N개와 같아지면 더 이상 연산자를 사용하지 않고, max와 min을 구해준다.
        sum_min=min(sum_min,arr)
        sum_max=max(sum_max,arr)
    else:   #각 연산자가 존재하면, 해당 연산자의 가능한 조합을 전부 탐색한다.
        if add:
            add-=1
            dfs(cnt+1,arr+a_arr[cnt])
            add+=1
        if sub:
            sub-=1
            dfs(cnt+1,arr-a_arr[cnt])
            sub+=1
        if mul:
            mul-=1
            dfs(cnt+1,arr*a_arr[cnt])
            mul+=1
        if div:
            div-=1
            dfs(cnt+1,int(arr/a_arr[cnt]))  #양수로 전환한 뒤 몫만 취하고 나머지는 버리므로, //가 아닌 /을 사용한다.
            div+=1
            
N=int(input())
a_arr=list(map(int,sys.stdin.readline().strip().split()))
add,sub,mul,div=map(int,sys.stdin.readline().strip().split())
sum_min=1e9
sum_max=-1e9

dfs(1,a_arr[0])    
print(sum_max)
print(sum_min)