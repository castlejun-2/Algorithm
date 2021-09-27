N,M=map(int,input().split())
dic={}                      //hash를 통해 값을 찾기 위해 튜플형{}로 선언
list=[]                     //듣도 보도 못한 list를 담기 위해 리스트형[]로 선언
for i in range(1,N+1):
    name=input()  
    dic[name]=i             //key:value를 통해 dic에 값을 저장
for _ in range(M):
    name=input()
    if name in dic.keys():  //name이라는 key가 dic에 존재한다면 list에 name을 추가
        list.append(name)
list.sort()                 //사전순으로 정렬하기 위해 정렬
print(len(list))            //길이를 출력
for i in list:              //list에 사전순으로 출력
    print(i)
