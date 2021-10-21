from itertools import combinations      #가능한 조합을 구하기 위한 함수

T=int(input())
m_list=[list(map(int,input().split())) for _ in range(T)]
members = [i for i in range(T)]         #멤버의 이름
team=list(combinations(members, T//2))  #가능한 팀의 조합 -> ex) 4C2, 6C2
score_gap=[]
for i in range(len(team)//2):
    select_team = team[i]            #가능한 팀 조합에서 팀 하나 선택, 이 때 앞의 절반 i 팀과 -i-1 팀이 대항된다
    start=0                          #start team 능력치
    for j in range(T//2):
        member=select_team[j]        #멤버 선택
        for k in select_team:
            start+=m_list[member][k] #멤버와의 시너지 합
            
    select_team = team[-i-1]    
    link=0                           #link team 능력치
    for j in range(T//2):
        member=select_team[j]
        for k in select_team:
            link+=m_list[member][k]     #멤버와의 시너지 합
    score_gap.append(abs(start-link))   #start team과 link팀의 격차 저장
print(min(score_gap))                   #가장 적은 스코어 격차 출력
