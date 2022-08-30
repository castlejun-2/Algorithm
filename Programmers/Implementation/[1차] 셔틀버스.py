def solution(n, t, m, timetable):
    answer = ''
    time = []
    last_time=540                 #첫 배차시각 09:00 으로 설정
    
    for tt in sorted(timetable):
        H,M=map(int,tt.split(':'))
        time.append(H*60+M)       #시간을 정수로 수치화
        
    for i in range(540,1440,t):   #"09:00" 부터 "23:59"까지 t분 간격으로 배차 운영
        if n==1:                  #마지막 탑승인원 확인 전에 반복 종료
            last_time=i           #마지막 탑승 시간 측정
            break
        now=m                     #현재 시각 최대 탑승 인원
        cnt=0
        for t in time:
            if t<=i and now:      #대기열에 있는 탑승 가능 인원 탑승
                now-=1            
                cnt+=1            
        time=time[cnt:]           #탑승 한 인원 제외
        n-=1                      #배차 횟수 감소
        
    if len(time) < m:             #막차에 탈 수 있는 인원이 여유가 있다면 막차 탑승
        answer=str(last_time//60).zfill(2)+':'+str(last_time%60).zfill(2)
    else:                         #마지막 차에 탈 수 있는 인원의 여유가 없다면
        if time[m-1]>last_time:   #대기열의 탑승 가능 마지막 인원이 막차보다 늦다면 막차 탑승
            answer=str(last_time//60).zfill(2)+':'+str(last_time%60).zfill(2)
        else:                     #대기열의 탑승 가능 마지막 인원이 막차보다 빠르다면 탈 수 있는 대기열보다 1분 빠르게 탑승
            answer=str((time[m-1]-1)//60).zfill(2)+':'+str((time[m-1]-1)%60).zfill(2)
    return answer
