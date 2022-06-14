N=int(input())
K=int(input())
sensor=list(map(int,input().split()))
sensor.sort()
stack=[]

if N<=K:    #집중국의 위치가 센서보다 많으면 센서의 각 위치에 집중국을 건설하면 됨으로 0을 출력한다.
    print(0)
else:
    for i in range(1,N):    #이웃하는 각 센서의 합을 구한다.
        stack.append(sensor[i]-sensor[i-1])

    stack.sort()    
    for _ in range(K-1):    #평면에서 K개로 구간을 나누는것이므로 거리가 가장 먼 순서대로 K-1개의 연결지점을 끊는다.
        stack.pop()

    print(sum(stack))   #남은 각 지점들의 거리의 합을 출력하여준다.
