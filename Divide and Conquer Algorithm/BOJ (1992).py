N=int(input())

m_list=[list(map(int,input())) for _ in range(N)]

def QuadTree(x,y,n):
    if n==1:
        return str(m_list[x][y])                            #n==1 이면 str형으로 변환 후 return
    image=[]                                                #출력 이미지 선언                            
    for i in range(x,x+n):
        for j in range(y,y+n):
            if m_list[x][y]!=m_list[i][j]:                  #범위 이내에 통일 되지 않은 값이 존재한다면 다시 구역을 나누어 탐색
                image.append('(')
                image.extend(QuadTree(x,y,n//2))            #왼측 상단 탐색
                image.extend(QuadTree(x,y+n//2,n//2))       #오른쪽 상단 탐색
                image.extend(QuadTree(x+n//2,y,n//2))       #왼쪽 하단 탐색
                image.extend(QuadTree(x+n//2,y+n//2,n//2))  #오른쪽 하단 탐색
                image.append(')')
                return image                                #나누어 탐색한 지역의 Object 삽입
    return str(m_list[x][y])                                #범위 이내의 값이 모두 같으면 가장 맨 앞 값을 str형으로 변환 후 return
    
print("".join(QuadTree(0,0,N)))                             #리스트로 받은 값의 구분자들을 모두 제거하여 한줄로 출력
