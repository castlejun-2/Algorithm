def factorial(N):                                           #factorial 함수를 재귀함수로 구현한다.
    if N>1:
        return N*factorial(N-1)
    else:
        return 1
      
N=int(input())
for _ in range(N):
    a,b=map(int,input().split())
    R=(int) (factorial(b)/(factorial(a)*factorial(b-a)))    #C(n,k)의 문제이므로 n!/k!*(n-k)! 로 계산한다.
    print(R)                                                #int형으로 형변환 한 결과값을 출력한다.
