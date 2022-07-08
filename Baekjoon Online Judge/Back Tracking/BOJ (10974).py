N=int(input())
visited=[0]*N

def back(arr):
    if len(arr)==N: #길이가 N이 되면 출력
        print(" ".join(map(str,arr)))
        return
    else:
        for i in range(1,N+1):  #앞의 값부터 append
            if not visited[i-1]:    #방문되어 있지 않은 경우
                visited[i-1]=1
                arr.append(i)
                back(arr)
                arr.pop()   #방문 후 요소 제거
                visited[i-1]=0 
    
for i in range(1,N+1):  #가장 앞의 값부터 시작
    visited[i-1]=1 
    arr=[]
    arr.append(i)
    back(arr)
    arr.pop()
    visited[i-1]=0
