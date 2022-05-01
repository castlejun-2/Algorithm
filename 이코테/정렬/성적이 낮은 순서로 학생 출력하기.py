N=int(input())
score_list=[]

for i in range(N):
    name,score=map(str,input().split())
    score_list.append([name,int(score)])
score_list.sort(key=lambda x:x[1])

for name in score_list:
    print(name[0],end=' ')