#---Back Tracking(백트래킹) 방법---
from sys import stdin

def bfs(idx):
    if len(arr)==L: #만들어진 문자열의 길이가 L과 같은경우
        cnt_con=0
        cnt_vo=0
        for alpha in arr: 
            if alpha in vowel:
                cnt_vo+=1
            else:
                cnt_con+=1
        if cnt_vo>=1 and cnt_con>=2:  #자음과 모음의 갯수를 만족하는 경우
            print(''.join(arr))
    else:
        for i in range(idx,C):  #주어진 a_list의 index부터 주어진 문자의 갯수까지 탐색
            arr.append(a_list[i])
            bfs(i+1)  #백트래킹
            arr.pop() #백트래킹이 끝난 후 bfs 탐색 이전에 추가한 값은 삭제
        
L,C=map(int,stdin.readline().split())
a_list=list(map(str,stdin.readline().split()))
a_list.sort()
vowel=['a','e','i','o','u']
arr=[]
checked=[0]*C
bfs(0)

#---Combination(조합) 방법---
#조합방법은 하나하나 가능한 조합을 만들지 않고 함수로 사용하여 일괄적으로 만든것이 위의 방법과 차이가 있다.
from sys import stdin
from itertools import combinations

L,C=map(int,stdin.readline().split())
a_list=list(map(str,stdin.readline().split()))
a_list.sort()
vowel=['a','e','i','o','u']
com_list=combinations(a_list,L) #a_list에 주어진 문자들로 길이 L의 문자열 조합
for cipher in com_list: #만들어진 조합중 하나의 조합 선택
    cnt_con=0
    cnt_vo=0
    for list_v in cipher: #해당 조합의 자음과 모음 갯수 탐색
        if list_v in vowel:
            cnt_vo+=1
        else:
            cnt_con+=1
    if cnt_vo>=1 and cnt_con>=2:  #자음과 모음의 갯수 만족시 출력
        print(''.join(cipher))
