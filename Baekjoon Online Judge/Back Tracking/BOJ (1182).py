from sys import stdin

N,S=map(int,stdin.readline().split())
n_list=list(map(int,stdin.readline().split()))
cnt=0


def back(idx,sub_sum):
    global cnt
    
    if idx==N:
        return
    
    sub_sum+=n_list[idx]                #현재 n_list[idx]에 기존의 sub_sum의 값을 더한다.
    
    if sub_sum==S:                      #sub_sum이 S와 같으면 cnt를 1 증가시켜준다.
        cnt+=1
    back(idx+1,sub_sum)                 #현재 n_list[idx]의 값을 포함하는 경우의 subset
    back(idx+1,sub_sum-n_list[idx])     #현재 n_list[idx]의 값을 포함하지 않은 경우의 subset
        
back(0,0)
print(cnt)
