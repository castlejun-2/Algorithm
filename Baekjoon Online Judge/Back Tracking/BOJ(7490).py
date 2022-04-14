from sys import stdin

T=int(stdin.readline().strip())

def check(arr): #N만큼의 길이에 도달하면, eval 함수를 통해 해당 문자열의 결과가 0인지 확인한다.
    temp_arr=(''.join(map(str,arr.split(' '))))
    if eval(temp_arr)==0:   # *eval*: 문자열인 계산식을 계산해주는 함수
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
    N=int(stdin.readline().strip()) #N이 3<=N<=9 이므로 완전탐색으로 풀어도 시간초과가 나지 않는다.
    
    #ASCII 코드 순서로 완전탐색을 한다
    space_dfs("1",1)    
    sum_dfs("1",1)
    mis_dfs("1",1)

    print()