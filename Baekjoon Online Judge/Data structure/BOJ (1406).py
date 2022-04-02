from sys import stdin
from collections import deque

block1 = list(map(str,stdin.readline().strip()))      #block을 2개 생성하여 ㅁㅁ을 둔다. 이 때 ㅁㅁ 사이가 cursor 즉, ㅁlㅁ 에서 l이 커서가 된다.
block2 = deque()
M = int(stdin.readline())

for command in stdin:
    if command[0]=='P':                               #커서의 왼쪽에 값이 추가됨으로 앞의 블록의 끝에 값이 추가된다.
        block1.append(command[2])
    elif command[0]=='L':                             #왼쪽 블록의 끝 값이 오른쪽 블록의 앞으로 이동하면 이는 커서가 왼쪽으로 이동하는 효과를 얻는다.
        if block1:
            block2.appendleft(block1.pop())
    elif command[0]=='D':                             #오른쪽 블록의 앞의 값이 왼쪽 블록의 끝 값으로 이동하면 이는 커서가 오른쪽으로 이동하는 효과를 얻는다.
        if block2:
            block1.append(block2.popleft())
    elif command[0]=='B':                             #커서의 왼쪽에 값이 삭제됨으로 앞의 블록의 끝의 값이 삭제된다.
        if block1:
            block1.pop()
print(''.join(block1+list(block2)))                   #deque을 list로 바꿔주어 출력하여준다.
