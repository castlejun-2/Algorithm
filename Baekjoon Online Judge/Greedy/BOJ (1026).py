N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

sum = 0
for i in range(N):          #B는 정렬 할 수 없으므로 다음의 방법 사용
    sum += min(A) * max(B)  #A의 최소값과 B의 최대값을 곱한다
    A.pop(A.index(min(A)))  #A의 최소값을 갖는 index pop()
    B.pop(B.index(max(B)))  #B의 최대값을 갖는 index pop()
    
print(sum)
