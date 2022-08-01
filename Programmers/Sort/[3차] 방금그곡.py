def solution(m, musicinfos):
    answer = []
    num = 0
    for music in musicinfos:
        start,end,name,sheet=music.split(',')
        
        start=list(map(int,start.split(':')))
        end=list(map(int,end.split(':')))
        
        playtime=(end[0]-start[0])*60+(end[1]-start[1]) #재생 시간
        cnt=sheet.count('#')    #샵의 갯수
        if not playtime%(len(sheet)-cnt):   #전체 악보
            total_sheet=(playtime//(len(sheet)-cnt))*sheet+sheet[:(playtime%(len(sheet)-cnt))]
        else:
            total_sheet=(playtime//(len(sheet)-cnt))*sheet+sheet[:(playtime%(len(sheet)-cnt))+cnt]

        if m in total_sheet:    #만약 m이 전체 악보에 존재한다면
            if cnt:     #샵의 여부에 따른 예외처리 로직
                arr=list(map(str,total_sheet.split(m)))
                for k in range(1,len(arr)):
                    if arr[k] and arr[k][0]=='#':
                        continue
                    else:
                        answer.append([playtime,num,name])
                        break
            else:
                answer.append([playtime,num,name])
        num+=1  #먼저 입력된 음악을 판단하기 위한 변수
    if not answer:
        return "(None)"
    else:
        return sorted(answer,key=lambda x:(-x[0],x[1]))[0][2]   #조건순으로 정렬
