N=int(input())
m_list=[]
for _ in range(N):
    K=int(input())
    m_list.append(K)
max=m_list[-1]    #최대값을 가장 마지막 값으로 설정
cnt=0             #감소 횟수 Count
for i in range(N-2,-1,-1):  #N-1번째 index부터 0까지 탐색
    if m_list[i]>=max:      #i의 index의 m_list값이 현재 최대값 보다 크다면
        cnt+=m_list[i]-max+1 #cnt는 값의 차이에 +1만큼 증가
        max-=1               #max값은 가장 적게 차이나도록 해야하므로 현재 최대값에 -1
    else:
        max=m_list[i]        #그 외에 현재 m_list의 값이 max보다 작다면 max값은 i의 index를 갖는 m_list값으로 변경
print(cnt)                   #감소 횟수 출력
