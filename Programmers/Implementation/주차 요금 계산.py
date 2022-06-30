def solution(fees, records):
    record={}   #차량의 입-출차 정보 저장
    cars=[] #차량 번호 저장
    for r in records:
        time,car,status=r.split()
        if car not in record:  
            record[car]=[time]
            cars.append(car)
        else:   
            record[car].append(time)
    cars.sort()
    answer=[0]*len(cars)
    for car,val in record.items():
        total=0
        for i in range(1,len(val),2):
            HH_OUT,MM_OUT=map(int,val[i].split(":"))
            HH_IN,MM_IN=map(int,val[i-1].split(":"))
            if MM_OUT-MM_IN < 0:
                total+=(HH_OUT-HH_IN-1)*60+(60+MM_OUT-MM_IN)
            else:
                total+=(HH_OUT-HH_IN)*60+MM_OUT-MM_IN
        if len(val)%2==1:   #마지막 출차가 이루어 지지 않은 경우 처리
            HH_OUT,MM_OUT=23,59
            HH_IN,MM_IN=map(int,val[-1].split(":"))
            if MM_OUT-MM_IN < 0:
                total+=(HH_OUT-HH_IN-1)*60+(60+MM_OUT-MM_IN)
            else:
                total+=(HH_OUT-HH_IN)*60+MM_OUT-MM_IN  
        if total <= fees[0]:    #기본 시간 이하인 경우
            answer[cars.index(car)]=fees[1]
        else:   
            if (total-fees[0])%fees[2] ==0:
                answer[cars.index(car)]=fees[1]+(int((total-fees[0])/fees[2]))*fees[3]
            else:   #시간 올림 처리
                answer[cars.index(car)]=fees[1]+(int((total-fees[0])/fees[2])+1)*fees[3]
    return answer