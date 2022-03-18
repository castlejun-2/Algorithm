from sys import stdin

N,K=map(int,stdin.readline().split())
num_list=list(map(int,stdin.readline().strip()))
result=[]
delK=K

for i in range(N):
    while delK and result:  #만약 삭제돼야 할 값들이 전부 삭제 되었거나 작은 값들을 다 빼내서 result가 다 비어졌으면 종료
        if result[-1] < num_list[i]:  #넣으려는 값이 stack의 top보다 크면 기존 stack에 존재하던 값들을 pop
            result.pop()
            delK-=1
        else:
            break
    result.append(num_list[i])  #값 list에 추가 (추가되어도 작은 값이라면 다음 반복에서 삭제된다)
    
for i in range(N-K):
    print(result[i],end='') #큰 값부터 앞에 존재하므로, result에서 N-K개의 갯수만큼의 큰 값만 출력
