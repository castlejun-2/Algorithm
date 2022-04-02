def draw(n):
    if n==3:
        m_list[0][:3]=m_list[2][:3]=['*']*3   
        m_list[1][:3]=['*',0,'*']   #공백은 리스트의 값으로 넣을 수 없으므로 0을 넣어두고 출력 때 0은 공백으로 출력되도록 한다.
        return
    a=n//3                    #n/3으로 한다면 a는 float형이 되고, 이는 아래 range(a)에 넣지 못하게 됨으로 정수가 나올 수 있도록 몫을 구하는 //연산자를 사용한다.
    draw(a)
    for i in range(3):        #i는 높이를 반복한다
        for j in range(3):    #j는 넓이를 반복한다
            if i==1 and j==1:
                continue
            for k in range(a):
                m_list[a*i+k][a*j:a*(j+1)]=m_list[k][:a]  #k는 □ 이 전 칸의 □ 를 반복하여 j에 맞춰 해당 칸의 높이들을 복사하여 갖고온다. 

if __name__ == "__main__":
    N=int(input())
    m_list=[[0]*N for _ in range(N)]
    draw(N)
    for i in m_list:
        for j in i:
            if j==0:
                print(' ',end = '')
            else:
                print(j,end='')
        print()
        
# □ □ □
# □ ■ □
# □ □ □
# 라고 생각하고, ■ 에는 빈 란이 들어간다고 생각한다. 이 때 n이 증가하면 위 그림이 한 set로 다시 저 □에 들어가 반복 시킨다.
