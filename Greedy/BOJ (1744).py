N=int(input())
list_p=[]
list_n=[]
result=0
for i in range(N):
    K=int(input())
    if K>1:
        list_p.append(K)                #양수 list에 값을 이어나간다.
    elif K==1:                          #1인 값은 더해주는 것이 최선이므로 따로 더해두고 리스트에 추가시키지 않는다
        result+=1
    else:
        list_n.append(K)                #음수 list에 값을 이어나간다.
list_p.sort(reverse=True)               #양수를 내림차순으로 정렬하여 높은수들끼리 곱해줄 수 있도록 해준다.
list_n.sort()                           #음수는 오름차순으로 정렬하여 절대값이 높은 음수들끼리 곱해줄 수 있도록 해준다.

#양수 list 계산
if len(list_p)%2==0:                    #길이가 짝수일 경우 리스트들을 쌍으로 묶어 곱해준다.                    
    for i in range(0,len(list_p),2):    
        result+=list_p[i]*list_p[i+1]
else:                                   #길이가 홀수일 경우 곱해주고 난 후 가장 작은 양수의 값은 더해준다.
    for i in range(0,len(list_p)-1,2):
        result+=list_p[i]*list_p[i+1]
    result+=list_p[len(list_p)-1]
    
#음수 list 계산    
if len(list_n)%2==0:                    #길이가 짝수일 경우 리스트들을 쌍으로 묶어 곱해준다.
    for i in range(0,len(list_n),2):    
        result+=list_n[i]*list_n[i+1]
else:                                   #길이가 음수일 경우 음수 중 절대값이 가장 작은 마지막 값은 더해준다.
    for i in range(0,len(list_n)-1,2):
        result+=list_n[i]*list_n[i+1]
    result+=list_n[len(list_n)-1]
print(result)                           #최종결과를 출력한다.
