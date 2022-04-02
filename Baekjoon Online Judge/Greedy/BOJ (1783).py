if __name__=="__main__":
    N,M=map(int,input().split())
    if N==1:              #N==1인 경우에는 M과 관계없이 맨 처음의 위치밖에 방문하지 못한다.
        print(1)
    elif N==2:            #N==2인 경우, 2,3 번 규칙을 이용하여 아래의 조건에 맞게 방문 할 수 있다.
        if M<3:
            print(1)
        elif M<5:
            print(2)
        elif M<7:
            print(3)
        else:
            print(4)
        #print(int(min(4,(M+1)/2))) 와 같은 기능이지만, min은 함수를 사용하는것이므로 속도는 위의 코드가 더 빠르다.
    elif N>=3:
        if M<7:
            if M<5:
                print(M)    
            else:
                print(4)    #3<=N, 5<=M<=6 인 경우는 4의 값을 얻는다
        else:
            print(M-2)      #3<=N 이고 M>=7인 경우는 높이에 상관없이 1,4번 규칙을 반복하는것이 가장 효율적이므로 규칙규약으로 인해 2칸을 움직인 경우를 빼준 M-2번의 칸을 방문하게 된다.
