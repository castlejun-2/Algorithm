N=int(input())
M=int(input())
button=[]
if M:
    button=list(map(str,input().split()))

answer=abs(100-N)

for i in range(1000000):    #0부터 백만까지, 입력 가능한 채널의 버튼을 입력한다.
    flag = True
    
    for s in str(i):
        if s in button:     #누를 수 없는 번호가 있다면 반복을 멈추고 다음 Target을 찾는다.
            flag=False
            break
    
    if flag:                #모두 누를 수 있는 채널이라면, 해당 채널에서 N까지 도달하는데 누르는 횟수를 입력한다.
        answer=min(answer,abs(N-i)+len(str(i)))
print(answer)