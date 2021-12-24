N,M = map(int,input().split())
b_list = []

def back():
    if len(b_list)==M:
        print(' '.join(map(str,b_list)))
        return
    else:
        for i in range(1,N+1):
            b_list.append(i)
            back()
            b_list.pop()
back()
