from sys import stdin

N,M = map(int,stdin.readline().split())
b_list = []

def back(k):
    if len(b_list) == M:
        print(" ".join(map(str,b_list)))  #b_list의 길이가 M이 되면 출력
    else:
        for t in range(k,N+1):
            if (t>=k):            #인자로 받은 k의 수보다 t가 크거나 같을 때 b_list에 추가 
                b_list.append(t)
                back(t)
                b_list.pop()      #백트래킹을 마치고 삽입된 t를 삭제

back(1)
