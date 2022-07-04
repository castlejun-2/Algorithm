def solution(record):
    user={} #dictionary 자료 구조를 통해 사용자 nickname 관리
    order=[]    #order를 통해 in과 out을 관리
    answer = []
    for re in record:
        tmp_re=list(map(str,re.split()))
        if tmp_re[0]=="Leave":
            order.append([tmp_re[0],tmp_re[1]])
        else:   #들어오거나 change 되면 해당 userid의 nickname으로 변경
            user[tmp_re[1]]=tmp_re[2]
            order.append([tmp_re[0],tmp_re[1]])
    for o in order:
        if o[0]=='Enter':
            answer.append(user[o[1]]+'님이 들어왔습니다.')
        elif o[0]=='Leave':
            answer.append(user[o[1]]+'님이 나갔습니다.')
    return answer