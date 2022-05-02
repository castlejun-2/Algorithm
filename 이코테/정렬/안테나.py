from sys import stdin

N=int(stdin.readline().strip())
home_list=list(map(int,stdin.readline().strip().split()))
home_list.sort()

if (len(home_list) % 2 ) == 0:  #이 때 집의 위치가 짝수이면 중간 두 집이 최소인데, 이 때는 index가 더 낮은 집을 선택해야하므로 -1을 한다.
    print(home_list[(len(home_list)//2)-1])
else:   #항상 중간에 있는 집에 위치 할 때 최소값을 갖는다.
    print(home_list[len(home_list)//2])