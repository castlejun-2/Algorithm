from sys import stdin
input=stdin.readline                        #성능 향상을 위해 readline으로 읽어준다.

def SetDfs(start, dfslist):                 #깊이 우선 탐색(DFS)를 실행시키는 함수
    for i in dfslist[start]:
        if i not in visited:
            visited.append(i)               #방문한 node를 visited list에 추가하여준다.
            SetDfs(i, dfslist)              #방문한 node에 연결된 node들을 다시 깊이 우선탐색 하도록 설정
            
dfslist = {}                                # ex) dfslist={ 1:{3,4,5}, 3:{4,5}, 5:{1,2,7} } 과 같이 key&value로 저장되도록 tuple로 구성
visited = []                                # 방문한 node들을 저장할 visited list 구성

for i in range(int(input())):
    dfslist[i+1] = set()                    # 각 key에 맞는 value에 값을 추가할 수 있도록 각 key를 set()을 통해 구성
for i in range(int(input())):
    first, second=map(int,input().split())
    dfslist[first].add(second)              # 각 key에 맞는 value들을 add로 추가
    dfslist[second].add(first)               

SetDfs(1, dfslist)                          # 1번 comuter부터 깊이우선탐색(DFS) 시작
print(len(visited)-1)                       # 1번을 제외한 visited에 들어있는 node들의 갯수 출력
