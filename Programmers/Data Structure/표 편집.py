def solution(n, k, cmd):
    now=k
    answer=['O']*n
    table={i:[i-1,i+1] for i in range(n)}
    table[0]=[None,1]
    table[n-1]=[n-2,None]
    delCell=[]
    
    for ins in cmd:
        if ins=='C':  #삭제의 경우
            answer[now]='X'
            prevIdx,nextIdx=table[now]
            delCell.append([prevIdx,now,nextIdx])
            if nextIdx==None: #현재 index의 다음 값이 없을 경우
                now=prevIdx   #전 index를 현재 index로 설정
            else:
                now=nextIdx   #그렇지 않을 경우 다음 index를 현재 index로 설정
            if prevIdx==None: #전 index가 존재하지 않을 경우
                table[nextIdx][0]=None  #다음 노드의 전 index를 None으로 설정
            elif nextIdx==None:
                table[prevIdx][1]=None  #다음 노드가 없을 경우 전 노드의 다음 index를 None으로 설정
            else: #그렇지 않은경우 전 노드와 다음 노드를 연결
                table[nextIdx][0]=prevIdx
                table[prevIdx][1]=nextIdx
                
        elif ins=='Z':  #복구의 경우
            prevIdx,idx,nextIdx=delCell.pop() #마지막에 삽입된 값 가져오기
            answer[idx]='O'
            if prevIdx==None: #전 index가 None이였을 경우
                table[nextIdx][0]=idx #다음 노드의 전 index를 자신으로 설정
            elif nextIdx==None: #다음 index가 None이였을 경우
                table[prevIdx][1]=idx #전 노드의 다음 index를 자신으로 설정
            else: #그렇지 않은 경우 전 노드를 자신에게 연결 및 다음 노드 또한 자신에게 연결
                table[prevIdx][1]=idx
                table[nextIdx][0]=idx
        else:
            instruction,value=ins.split(' ')
            value=int(value)
            if instruction=='D':  #아래로 갈 경우 value만큼 now들의 next로 이동
                for _ in range(value):
                    now=table[now][1]
            else: #위로 갈 경우 value만큼 now들의 prev로 이동
                for _ in range(value):
                    now=table[now][0]
    return "".join(map(str,answer))
