import sys
input=sys.stdin.readline

S=input().strip()
T=input().strip()

lenS=len(S)
lenT=len(T)

for i in range(lenT-1,lenS-1,-1):   #T가 S가 될 수 있는지 탐색
    c=T[i]
    T=T[:i]
    
    if c=='B':                      #마지막 문자가 B였다면 뒤집는다
        T=T[::-1]
print(1 if S==T else 0)