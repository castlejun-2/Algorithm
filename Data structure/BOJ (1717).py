from sys import stdin
import sys
sys.setrecursionlimit(100000)           #재귀의 깊이를 넉넉하게 설정하여준다.

def union(x,y):                         #분리되어 있는 집합을 합쳐주는 함수
    a=find(x)
    b=find(y)
    if a==b:
        return
    elif a>b:
        n_list[a]=b
    else:
        n_list[b]=a
        
def find(k):                            #해당 노드의 루트노드를 찾는 함수
    if n_list[k]==k:                    #노드번호와 해당 index의 값이 같으면 루트노드 이므로 index 반환
        return k
    parent=find(n_list[k])              #반환된 값을 해당 노드번호의 루트노드로 설정
    n_list[k]=parent
    return n_list[k]                    #k의 root node를 반환
        
n,m = map(int,stdin.readline().split())
n_list = []
for i in range(n+1):n_list.append(i)

for i in range(m):
    op,a,b = map(int,stdin.readline().split())
    if not op:                          #합집합 연산이면 a와 b를 합친다.
        union(a,b)
    else:                               #확인하는 연산을 통해 YES/NO를 출력하여준다.
        x=find(a)
        y=find(b)
        if x==y:
            print("YES")
        else:
            print("NO")
