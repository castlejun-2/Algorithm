p_list=list(input())          #받은 문자열들을 list형태로 저장
s=[]                          #파이프의 갯수를 나타낼 배열 선언
cnt=0
for i in range(len(p_list)):  #list의 길이만큼 반복
    if p_list[i]=='(':        #'('일 경우 파이프라고 가정하고 파이프배열 s에 추가
        s.append('(')
    else:
        if p_list[i-1]=='(':  #')'일 경우 바로 전 항이 '('이면 레이저 이므로
            s.pop()           #전에 넣어주었던 파이프라고 가정한 '('을 pop 해주고
            cnt+=len(s)       #현재 pipe의 길이만큼 갯수가 증가하므로 cnt+=len(s)를 더해준다.
        else:
            s.pop()           #앞의 항이 ')'이고 또 그 다음항이 ')'일 경우는 파이프가 끝나는 지점이므로
            cnt+=1            #파이프를 빼준 후 파이프 갯수를 +1 증가시켜준다.
print(cnt)
