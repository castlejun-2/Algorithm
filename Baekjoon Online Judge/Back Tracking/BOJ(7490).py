from sys import stdin

T=int(stdin.readline().strip())

def check(arr):
    temp_arr=(''.join(map(str,arr.split(' '))))
    if eval(temp_arr)==0:
        return True
    else:
        return False
    
        
def space_dfs(arr,s):
    arr+=(" "+str(s+1))
    if((s+1)==N):
        if check(arr):
            print(arr)
    else:
        space_dfs(arr,s+1)
        sum_dfs(arr,s+1)
        mis_dfs(arr,s+1)

def mis_dfs(arr,s):
    arr+=("-"+str(s+1))
    if((s+1)==N):
        if check(arr):
            print(arr)
    else:
        space_dfs(arr,s+1)
        sum_dfs(arr,s+1)
        mis_dfs(arr,s+1)
                
def sum_dfs(arr,s):
    arr+=("+"+str(s+1))
    if((s+1)==N):
        if check(arr):
            print(arr)
    else:
        space_dfs(arr,s+1)
        sum_dfs(arr,s+1)
        mis_dfs(arr,s+1)
    
for i in range(T):
    N=int(stdin.readline().strip())
    
    space_dfs("1",1)
    sum_dfs("1",1)
    mis_dfs("1",1)

    print()