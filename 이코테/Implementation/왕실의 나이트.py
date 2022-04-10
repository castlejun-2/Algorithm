from sys import stdin

col,row=map(str,stdin.readline().strip())
moves=[(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,-1),(-2,1)] #이동 가능한 방향들
cnt=0

for move in moves:
    temp_col=chr(ord(col)+move[0])  #ASCII코드 값으로 변환하여, 이동한 열 확인
    temp_row=int(row)+move[1]   #int형으로 변환하여, 이동한 행 확인
    if 'a'<=temp_col<='h' and 1<=temp_row<=8:   #범위 내에 위치해 있으면 count +1
        cnt+=1
print(cnt)