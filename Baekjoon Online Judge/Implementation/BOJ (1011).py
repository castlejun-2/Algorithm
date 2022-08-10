T=int(input())
for _ in range(T):  #distance에 따른 최소 이동횟수의 증가 규칙이 1,1,2,2,3,3..이다
    x,y=map(int,input().split())
    cnt=1   #실제 distance 까지 도달 하기 위한 비교 값
    plus=1  #1,1,2,2,3,3 에서 각 1,2,3을 나타내는 값
    flag=0  #각 숫자가 두번 나왔는지를 계산해주는 flag 값
    distance=y-x  #distance 값
    answer=0  #최소 이동 횟수
    while cnt <= distance:  
        cnt+=plus   #증가하는 값만큼 cnt에 증가
        flag+=1
        if flag>1:  #숫자가 두번 나오면 증가하는 값 증가
            plus+=1
            flag=0
        answer+=1
    print(answer)
