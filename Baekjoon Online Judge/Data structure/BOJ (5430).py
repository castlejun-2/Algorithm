from sys import stdin
from collections import deque

T=int(stdin.readline())

for _ in range(T):
    func=list(map(str,stdin.readline().rstrip()))
    n=int(stdin.readline())
    n_list=deque(stdin.readline().rstrip()[1:-1].split(","))
    check=True
    reverse_cnt=0
    if n == 0:
        n_list.popleft()
        n_list=deque()
    for i in func:
        if len(n_list) == 0:
            if i == 'D':
                check=False
                print('error')
                break;
        elif i == 'R':  #시간 단축을 위해 R의 횟수를 축적해준 후 마지막에 뒤집는다.
            reverse_cnt+=1
        elif i == 'D':
            if reverse_cnt % 2 == 0:  #뒤집는 횟수가 짝수이면 뒤집지 않아도 되므로 가장 앞의 값을 빼준다
                n_list.popleft()
            else: #뒤집는 횟수가 홀수이면 뒤집어야 하므로 가장 뒤의 값을 빼준다.
                n_list.pop()
    if check: 
        if reverse_cnt % 2 == 0:  #뒤집는 횟수가 짝수이면 뒤집지 않고 출력해준다.
            print('['+','.join(n_list)+"]")
        else:
            n_list.reverse()  #뒤집는 횟수가 홀수이면 뒤집어서 출력해준다.
            print('['+','.join(n_list)+"]")
