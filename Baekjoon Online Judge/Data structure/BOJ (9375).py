from sys import stdin

N=int(stdin.readline())

if N==0:
    print(0)
else:
    for _ in range(N):
        T=int(stdin.readline())
        costume_list={}
        cnt_sum=1
        for i in range(T):  #각 의상 종류에 맞는 의상을 삽입
            costume,costume_type=map(str,stdin.readline().split())
            if costume_type in costume_list:
                costume_list[costume_type].append(costume)
            else:
                costume_list[costume_type] = [costume]
        for c in costume_list:  #의상 종류에 n개의 의상이 있다면 n개중 1개의 의상을 고르는 갯수와 아무것도 고르지 않을 수 있으므로 n+1을 곱해준다.
            cnt_sum*=len(costume_list[c])+1
        print(cnt_sum-1)    #단 모든 의상을 입지 않는 경우는 빼주어야 하므로 -1을 해준다.
