N=int(input())
solution=sorted(list(map(int,input().split())))

left,right=0,N-1
answer=[]
ans_sum=float('inf')

while left<right:     #N은 최대 100,000 이므로 O(N)으로 인해 시간초과에 걸리지 않는다.
    
    sum_val=solution[left]+solution[right]  
    
    if abs(sum_val)<ans_sum:      #음수값을 비교할 수 있으므로 절대값으로 값을 비교
        answer=[solution[left],solution[right]]     #차이가 더 적다면 값 갱신
        ans_sum=abs(sum_val)
        if ans_sum==0:            #만약 0이라면 즉시 반복 종료
            break
    
    if sum_val<0:       #양수쪽에 가까워 지기 위해 음수값을 갱신
        left+=1
    else:
        right-=1
        
print(*answer)
