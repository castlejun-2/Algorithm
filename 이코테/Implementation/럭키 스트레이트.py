from sys import stdin

num_list=list(map(int,stdin.readline().strip()))

half_sum=sum(num_list)
list_sum=0
if half_sum%2==1:   #합이 홀수이면 럭키스트레이트가 될 수 없다.
    print('READY')
else:
    for i in range(len(num_list)//2):   #전체 합의 절반과 가운데 index까지의 합을 비교한다
        list_sum+=num_list[i]
    if list_sum==half_sum//2:   #같으면 LUCKY
        print('LUCKY')
    else:                       #같지 않으면 READY를 출력한다.
        print('READY')