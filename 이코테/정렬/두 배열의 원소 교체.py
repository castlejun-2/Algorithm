N,K=map(int,input().split())
A_list=list(map(int,input().split()))
B_list=list(map(int,input().split()))

A_list.sort(reverse=True)
B_list.sort(reverse=True)
answer=0

for i in range(len(A_list)-K):
    answer+=A_list[i]
for i in range(K):
    answer+=B_list[i]

print(answer)