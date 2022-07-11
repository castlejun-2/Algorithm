con={'q': [0,0],'w': [0,1],'e': [0,2],'r': [0,3],'t': [0,4],'a': [1,0],'s': [1,1],'d': [1,2],'f': [1,3],'g': [1,4],'z': [2,0],'x': [2,1],'c': [2,2],'v': [2,3]}
vow={'y': [0,5],'u': [0,6],'i': [0,7],'o': [0,8],'p': [0,9],'h': [1,5],'j': [1,6],'k': [1,7],'l': [1,8],'b': [2,4],'n': [2,5],'m': [2,6]}

start_left,start_right=map(str,input().split())
arr=list(map(str,input()))
answer=0
idx=0

while idx<len(arr): #문자열의 길이만큼 반복
    if arr[idx]==start_left or arr[idx]==start_right: #현재 손가락이 있는 위치의 문자와 같다면
        answer+=1 #입력시간
        idx+=1  #인덱스 증가
    else:
        if arr[idx] in con: #자음 칸에 존재한다면
            now_x,now_y=con[start_left] #현재 손가락의 좌표
            left_x,left_y=con[arr[idx]] #해당 문자의 좌표
            answer+=abs(now_x-left_x)+abs(now_y-left_y) #이동시간
            start_left=arr[idx] #현재 손가락을 해당 문자의 좌표로 위치
        elif arr[idx] in vow: #모음 칸에 존재한다면
            now_x,now_y=vow[start_right]  #현재 손가락의 좌표
            right_x,right_y=vow[arr[idx]] #해당 문자의 좌표
            answer+=abs(now_x-right_x)+abs(now_y-right_y) #이동시간
            start_right=arr[idx]  #현재 손가락을 해당 문자의 좌표로 위치
        answer+=1   #입력시간
        idx+=1  #인덱스 증가
print(answer)
