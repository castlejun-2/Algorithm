def dfs():
    if len(list)==M:                      #M의 길이를 만족하면 출력
        print(' '.join(map(str,list)))    #map 함수를 통해 int형의 list들을 문자열로 변환시켜 출력
        return
    for i in range(1,N+1):                #i에 1부터 N까지 넣어주면서 list에 넣어준다
        if i not in list:                 #리스트에 들어있는 요소는 들어가지 않도록 설정
            list.append(i)
            dfs()                         #재귀함수를 통해 중복되지 않는 수열들을 출력
            list.pop()                    #재귀를 마치고 돌아온 리스트의 가장 마지막 값을 pop 해준 후 for문 반복

if __name__=="__main__":
    N,M=map(int,input().split())        
    list=[] 
    dfs()
