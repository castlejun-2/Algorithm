def check(i):
    for x in range(1,i):
        if abs(q_list[i]-q_list[x])==i-x or (q_list[x]==q_list[i]):   #대각선라인에 있거나 그 값이 안에 존재하는지 확인한다
            return 0
    else:
        return 1

def Nqueen(cidx): #각 자릿수를 하나씩 채워나가는 Nqueen함수 선언한다
    global cnt
    if N<cidx:
        cnt+=1
    else:
        for i in range(1,N+1):  #1번째 자릿수부터 시작한다
            q_list[cidx]=i      #cidx번째자릿수에 i를 삽입한다
            if check(cidx):     #해당 cidx 자릿수에 삽입한 값이 유효한 값인지 확인한다
                Nqueen(cidx+1)  #유효하다면 다음 자릿수로 진행, 유효하지 않으면 다음 i 값으로 넘어간다
            
N=int(input())
q_list=[0 for _ in range(N+1)]  #q_list[]로 비교하기 위해 0으로 N번째까지의 index를 미리 채워둔다
cnt=0                           #갯수를 count할 변수
Nqueen(1)                       #1번째 자리부터 탐색 시작
print(cnt)                      #최종 가능한 Nqueen 개수 출력
