#시간 초과 코드
# import copy

# def compare(score_array,info):
#     global answer,a_score,max_gap
#     t_score=a_score
#     score=0
#     for i in range(11):
#         if info[i] and score_array[i]:
#             if score_array[i] > info[i]:
#                 score+=(10-i)
#                 t_score-=(10-i)
#         elif score_array[i]:
#             score+=(10-i)
#     if score > t_score:
#         if max_gap <= score-t_score:
#             max_gap=score-t_score
#             answer=copy.deepcopy(score_array)
    
# def dfs(tarray,cnt,info):
#     if cnt==0:
#         compare(tarray,info)
#         return
#     else:
#         for i in range(11):
#             tarray[i]+=1
#             dfs(tarray,cnt-1,info)
#             tarray[i]-=1

# def solution(n, info):
#     global a_score
#     global answer
#     for i in range(11):
#         if info[i]:
#             a_score+=(10-i)
#     score=[0]*11
#     for i in range(11):
#         score[i]+=1
#         dfs(score,n-1,info)
#         score[i]-=1
#     if not answer:
#         answer=[-1]
#     return answer

# answer=[]
# max_gap=0
# a_score=0

from collections import deque
import copy

def bfs(n,info):
    q=deque([(0,[0]*11)]) #쏠 점수와 화살 상태를 담을 deque 배열
    res=[]
    max_gap=0
    
    while q:
        score,arrow=q.popleft() #높은 점수를 쏘는 경우의 수 부터 점수를 갱신해 나아간다.
        
        if sum(arrow) == n: #화살을 다 쏜 경우
            lion_score=0
            apeach_score=0
            for i in range(11):
                if arrow[i] > info[i]:  #해당 위치에 라이언이 더 많이 쏠 경우
                    lion_score+=(10-i)
                else:   
                    if info[i]: #해당 위치에 어피치가 더 많이 쏠 경우
                        apeach_score+=(10-i)
                        
            if lion_score > apeach_score: #라이언이 이긴 경우
                if max_gap <= lion_score - apeach_score: #최대 차이 값 
                    max_gap = lion_score - apeach_score
                    res.clear() #초기화 후 새로운 값 갱신
                    res.append(arrow)   #최대 차이 값이 같은 경우 나중에 들어온 arrow가 낮은 점수가 더 많다.
        elif sum(arrow) > n:    #주어진 화살보다 많이 쏘게 될 경우
            continue
        elif score==10: #화살이 남은 경우 모든 화살을 쏜다
            tmp=copy.deepcopy(arrow)
            tmp[score]=n-sum(tmp)
            q.append((11,tmp))
        else:
            tmp=copy.deepcopy(arrow)
            tmp[score]=info[score]+1
            q.append((score+1,tmp))     #해당 score에서 더 많이 쏘는 경우
            tmp2=copy.deepcopy(arrow)
            tmp2[score]=0
            q.append((score+1,tmp2))    #해당 score는 버리고 가는 경우
    return res                    
            
def solution(n, info):
    answer=bfs(n,info)
    if not answer:  #이기는 경우가 없을 때 -1 리턴
        return [-1]
    else:
        return answer[-1]

print(solution(9,[0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))