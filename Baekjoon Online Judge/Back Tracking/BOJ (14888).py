N = int(input())
n_list = list(map(int,input().split()))
a,s,m,d = map(int,input().split())
max_num = -1000000000
min_num = 1000000000

def dfs(i,num,add,sub,mul,div):   #깊이 우선 탐색을 통해서 모든 값들을 조사한다
    global max_num, min_num
    if i==N:                      #i가 N과 같아지면 최종값이 도출된것이므로, 최종값과 (최대,최소)값을 비교하여 수정한다.
        if num > max_num: 
            max_num = num
        if num < min_num:
            min_num = num
        return
    else:                         #연산이 존재하면 전부 확인하여본다.
        if add:
            dfs(i+1,num+n_list[i],add-1,sub,mul,div)
        if sub:
            dfs(i+1,num-n_list[i],add,sub-1,mul,div)
        if mul:
            dfs(i+1,num*n_list[i],add,sub,mul-1,div)
        if div:
            dfs(i+1,int(num/n_list[i]),add,sub,mul,div-1)

dfs(1,n_list[0],a,s,m,d)          #n_list의 첫번째 수와 연산자의 갯수를 인자로 갖고 탐색을 시작한다.
print(max_num)
print(min_num)
