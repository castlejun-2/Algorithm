def solution(msg):
    answer = []
    dic = { chr(i+65): i+1 for i in range(26) } #색인 번호
    last = 27
    i = 0
    while i < len(msg): #길이만큼 반복
        tmp = msg[i]
        flag = 0
        k = i+1 # i+1부터 문자열 덧셈
        while k < len(msg): #msg길이만큼 탐색
            if tmp+msg[k] in dic: #합친 문자열이 dic에 존재한다면
                tmp+=msg[k] #tmp를 해당 합친문자열로 수정
                flag=1  #flag 수정
                k+=1  #k값 증가 후 k번째 문자열도 이어붙혀 탐색
                i = k #그 다음 반복에서 k번째 index부터 탐색
            else:
                break
        if flag:  #가장 긴 사전에 존재하는 문자열 번호 출력
            answer.append(dic[tmp])
        else: #그렇지 않다면 i번째 index의 문자의 번호 출력
            answer.append(dic[msg[i]])
            i+=1  #i+1번째부터 재 탐색
        if i < len(msg):  #위에서 i가 1증가하여 len(msg)와 같아 질 수 있으므로
            dic[tmp+msg[i]] = last  #(w+c) 로직처리
            last+=1 #사전의 번호 증가
    return answer
