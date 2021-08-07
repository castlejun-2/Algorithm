import sys
input=sys.stdin.readline

l=[1,1]
for i in range(2,91):
    l.append(l[i-2]+l[i-1])    #append 함수를 이용하여 list에 동적할당 기법의 수를 더해준다.
n=int(input())                 #int형으로 형변환 하여 문자열로 입력받은 n을 정수형으로 바꿔준다.          
print(l[n-1])                  #0번째 index부터 저장되어 있으므로, n번째 이면 n-1 인덱스의 리스트 값을 출력한다.
