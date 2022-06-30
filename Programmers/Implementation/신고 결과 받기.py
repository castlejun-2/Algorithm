def solution(id_list, report, k):
    answer=[0]*len(id_list)
    d=dict()    #자신을 신고한 user 배열
    user=dict() #자신이 신고한 user 배열
    for id in id_list:  #존재하는 user들의 배열 생성
        d[id]=set()
        user[id]=set()
        
    for r in report:
        id,pid=r.split()
        d[pid].add(id)
        user[id].add(pid)
    for key,val in user.items():
        if len(val):
            for v in val:   #자신이 신고한 user
                if len(d[v]) >= k:  #신고한 user가 k명 이상에게 신고 당하면
                    for idx in range(len(id_list)):
                        if key==id_list[idx]:
                            answer[idx]+=1  #자신이 받을 메일에 +1
                            break
    return answer