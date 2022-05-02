def solution(N, stages):
    answer = []
    stage_fail_list=[0]*(N+1)
    stages.sort()
    personal=len(stages)
    before_fail=stages[0]
    temp_cnt=1
    
    #아래의 방법을 사용하지 않고 stages.count(i) 를 사용하여 해당 list에서 i의 값을 갖는 값을 계산 할 수 있음
    for i in range(1,len(stages)):  #앞의 스테이지부터 처리하여, 막힌 인원은 뒤에 스테이지를 가지 못하도록 반영
        if stages[i] != before_fail:    #클리어한 스테이지가 달라졌다면, 이 전 스테이지의 실패율 계산
            stage_fail_list[before_fail-1]=float(temp_cnt/personal) #현재 스테이지 까지의 생존수에 실패한 사람의 수를 나누어 실패율 저장
            personal-=temp_cnt
            temp_cnt=1
            before_fail=stages[i]
        else:
            temp_cnt+=1 #앞선 사람과 실패한 스테이지가 같다면 인원을 확장 후 진행
    if temp_cnt > 1:    #종료하지 못한 스테이지에 대한 처리가 이루어지지 않는 예외처리
        stage_fail_list[before_fail-1]=float(temp_cnt/personal)
    
    #temp_answer을 사용하지 않고 아래방법으로 해결 가능
    #answer=[i[1]+1 for i in answer]    
    temp_answer=[]
    for i in range(N):
        temp_answer.append([stage_fail_list[i],i])
    temp_answer.sort(key=lambda x:(-x[0],x[1])) #실패율에 따른 stage정보 저장
    
    for a in temp_answer:
        answer.append(a[1]+1)
    
    return answer