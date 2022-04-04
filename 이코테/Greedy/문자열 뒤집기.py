from sys import stdin

num_list=list(map(int,stdin.readline().strip()))
now=0
cnt=[0,0]

if num_list[0]:
    cnt[1]+=1
    now=1
else:
    cnt[0]+=1

for i in range(1,len(num_list)):
    if now==num_list[i]:
        continue
    else:
        now=num_list[i]
        cnt[now]+=1
print(min(cnt))