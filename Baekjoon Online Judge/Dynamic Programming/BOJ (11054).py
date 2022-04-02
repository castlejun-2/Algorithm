from sys import stdin

def find_left(n): #자기 자신보다 왼쪽에 있는 값 중 자신보다 작은 값들의 dp 값들을 자신과 더한다.
    temp_max=0
    for i in range(n):
        if tonic_list[i] < tonic_list[n]:
            temp_max=max(dp_left[i],temp_max)
    dp_left[n]+=temp_max
    
def find_right(n):  #자기 자신보다 오른쪽에 있는 값중 자신보다 작은 값들의 dp 값들을 자신과 더한다
    temp_max=0
    for i in range(n,N):
        if tonic_list[i] < tonic_list[n]:
            temp_max=max(dp_right[i],temp_max)
    dp_right[n]+=temp_max
    
N=int(stdin.readline())
tonic_list=list(map(int,stdin.readline().split()))
dp_left=[1]*N   #자기 자신을 포함하므로 1로 초기화
dp_right=[1]*N
dp_sum=[0]*N

for i in range(N):
    find_left(i)
    
for i in range(N-1,-1,-1):
    find_right(i)
    
for i in range(N):  #좌 우로 값들의 합을 저장하여준다.
    dp_sum[i]=dp_left[i]+dp_right[i]
    
print(max(dp_sum)-1)  #좌 우로 자신을 포함하여 값을 더해주었으므로, 1을 뺀 최종 값을 출력한다.
