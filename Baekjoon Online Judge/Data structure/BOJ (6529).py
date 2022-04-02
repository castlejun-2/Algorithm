from sys import stdin
while True:
    h_list=list(map(int,stdin.readline().split()))
    if not h_list[0]:
        break;
    stack=[]
    max_h=0
    for i in range(1,h_list[0]+1):
        expand=i-1
        while stack and stack[-1][0]>=h_list[i]:        #새로 비교할 높이가 stack의 top의 높이보다 작으면 히스토그램의 크기가 더 커질 수 없으므로 max값을 조정 
            h,expand=stack.pop()                        #stack의 top에 있던 높이와 영향을 끼칠 수 있는 index의 시작위치를 추출해온다
            tmp_width=h*(i-1-expand)                    #(stack의 top에 있던 높이) * (영향을 끼치는 영역) = 넓이 이므로 현재의 i에서 영향을 끼치는 시작점의 위치를 빼준 후 높히를 곱한다.
            max_h=max(max_h,tmp_width)                  #현재까지의 최대넓이와 비교하여 값을 갱신한다.
        stack.append([h_list[i],expand])                #새로 비교할 높이와 이 전 stack에서 가장 최근에 pop된 영향을 끼칠 수 있는 index의 시작위치를 계승받아 갱신한다. ex)만약 i는6일 때 마지막에 pop된 stack의 index가 2이면 이는 i=6일때의 높이가 index 2부터 6까지 영햐을 끼친다는 의미이다.
    for h,expand in stack:                              #배열의 길이만큼 돌고 stack에 남아있는 값들의 넓이를 계산하여 준다.
        max_h=max(max_h,h*(h_list[0]-expand))           #stack에 남아있는 h와 expand의 정보를 통해 최대 너비에서 자신이 영향을 끼치기 시작하는 index를 빼주면 총 영향을 미치는 너비가 나오기 때문에 이 값에 h를 곱해 넓이를 구해주고 만약 이 값이 기존의 max 높이보다 크다면 갱신하여준다.
    print(max_h)
