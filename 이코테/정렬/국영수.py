from sys import stdin
N=int(stdin.readline().strip())
score_list=[]

for i in range(N):
    name,korean,english,math=map(str,stdin.readline().strip().split())
    score_list.append([name,int(korean),int(english),int(math)])

score_list.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))   #lambda를 사용하여, 정렬 순서를 선정

for i in range(N):
    print(score_list[i][0])