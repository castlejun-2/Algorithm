n=5
build_frame=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

def check_answer(answer):
    for x,y,structure in answer:
        if structure==1:    #보인 경우
            if  [x,y-1,0] in answer or [x+1,y-1,0] in answer or [x-1,y,1] in answer and [x+1,y,1] in answer:
                continue
            return False
        else:   #기둥인 경우
            if y==0 or [x-1,y,1] in answer or [x,y-1,0] in answer or [x,y,1] in answer:
                continue
            return False
    return True

def solution(n, build_frame):
    answer=[]
    for build in build_frame:
        x,y,structure,operation=map(int,build)
        if operation==0:    #삭제
            answer.remove([x,y,structure])  
            if check_answer(answer):    #삭제가 성공했으면 진행
                continue
            answer.append([x,y,structure])  #실패했으면 원상복구
        else:
            answer.append([x,y,structure])  
            if check_answer(answer):    #삽입이 성공했으면 진행
                continue
            answer.remove([x,y,structure])  #실패했으면 원상복구
    answer.sort()   #정렬
    return answer    #sorted(answer)   !sorted는 정렬된 결과를 반환

print(solution(n,build_frame))