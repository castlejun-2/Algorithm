def back():
    if len(list)==M:
        print(' '.join(map(str,list)))
        return
    for i in range(1,N+1):
        if i not in list:             #i가 list에 존재하지 않을 때 삽입
            if list and list[-1]<i:   #list에 값이 들어있다면, i는 list의 가장 마지막값 보다 클때만 삽입
                list.append(i)        #list에 값을 삽입
                back()                #재귀를 통해 다시한번 back 함수 실행
                list.pop()            #길이가 M이 되었을 때 출력후 return 되었다면 가장 마지막 값 pop
            elif not list:            #list가 비어있다면 일단 값 삽입 진행
                list.append(i)
                back() 
                list.pop()
        
N,M=map(int,input().split())
list=[]
back()
