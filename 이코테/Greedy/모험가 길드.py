from sys import stdin

N=int(stdin.readline().strip())
adventure_list=list(map(int,stdin.readline().split()))

adventure_list.sort()
group=0
people=0

for fear in adventure_list:
    people+=1
    if people >= fear:  #인원이 채워지면 그룹을 형성지어 모험을 출발
        group+=1
        people=0    #모험을 출발하였으므로, 사람을 처음부터 다시 구한다.
print(group)