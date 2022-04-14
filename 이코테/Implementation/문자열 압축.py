def solution(s):
    minlen=len(s)
    for i in range(1,(len(s)//2)+1):
        temp_s=[s[k:k+i] for k in range(0,len(s),i)]    #1부터 s길이의 절반까지 만큼 split 가능한 조합들을 찾는다.
        last_str=temp_s[0]
        cnt=len(s)
        t_cnt=1
        for k in range(1,len(temp_s)):  
            if temp_s[k]==last_str: #길이가 이어진다면 t_cnt를 증가
                t_cnt+=1
            else:   #길이가 끊어졌다면, 마지막 문자열을 바꿔주고, t_cnt에 따른 문자열 길이 조정
                last_str=temp_s[k]
                if t_cnt >= 1000:
                    cnt+=4
                    cnt-=(i*(t_cnt-1))
                    t_cnt=1
                elif t_cnt >= 100:
                    cnt+=3
                    cnt-=(i*(t_cnt-1))
                    t_cnt=1
                elif t_cnt >=10:
                    cnt+=2
                    cnt-=(i*(t_cnt-1))
                    t_cnt=1
                elif t_cnt>1:
                    cnt+=1
                    cnt-=(i*(t_cnt-1))
                    t_cnt=1
                
        if t_cnt >= 1000:   #문자열이 끝까지 끊기지 않았을 경우 예외처리
            cnt+=4
            cnt-=(i*(t_cnt-1))
        elif t_cnt >= 100:
            cnt+=3
            cnt-=(i*(t_cnt-1))
        elif t_cnt >=10:
            cnt+=2
            cnt-=(i*(t_cnt-1))
        elif t_cnt>1:
            cnt+=1
            cnt-=(i*(t_cnt-1))
        minlen=min(minlen,cnt)  #현재까지의 cnt값과 maxlen값을 비교하여 더 작은 값을 결과값에 삽입
    answer = minlen
    return answer