from sys import stdin

num_list=list(map(int,stdin.readline().strip()))
num_list.sort()
idx=0
for i in num_list:  #0인 경우들을 전부 예외처리로 넘겨준다.
    if i==0:
        idx+=1
    else:
        break
sum=num_list[idx]   #곱셈을 위해 초기값으로 0 다음으로 큰 숫자를 선언하여준다.   

for i in range(idx+1,len(num_list)):
    if num_list[i]>1:   #1보다 크면 곱해준다.
        sum*=num_list[i]
    elif num_list[i]==1:    #1이면 더해준다.
        sum+=1
print(sum)
    
        