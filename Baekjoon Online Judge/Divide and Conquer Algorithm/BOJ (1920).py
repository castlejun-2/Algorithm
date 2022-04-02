def div(i,start,end):                    #인자로(찾아야 할 값, 시작 인덱스, 끝 인덱스) 를 전달한다.
    if start > end:                      #찾아야 할 값을 찾지 못해 넘어가버린다면 0을 반환한다.
        return 0
    index=(start+end)//2                 #중간을 기준으로 2로 나누어준 index를 설정한다.
    if i==list_v[index]:                 #찾아야 할 값을 찾았다면 1을 return 하여준다.
        return 1
    elif i<list_v[index]:                #찾아야 할 값보다 중간의 값이 더 크다면 아래 범위를 탐색한다.
        return div(i,start,index-1)
    else:                                #찾아야 할 값보다 중간의 값이 더 작으면 윗 범위를 탐색한다.
        return div(i,index+1,end)
        
if __name__=="__main__":
    N=int(input())
    list_v=sorted(map(int,input().split()))    #정렬된 값을 받아준다.
    T=int(input())
    list_c=(map(int,input().split()))
    start=0
    end=len(list_v)-1
    for i in list_c:
        print(div(i,start,end))                #리스트에서 값을 하나씩 꺼내서 확인하여준다.
