from itertools import permutations

def solution(n, weak, dist):
    dist_list=list(permutations(dist))
    weak_len=len(weak)
    answer=len(dist)+1    
    for i in range(weak_len):
        weak.append(weak[i]+n)
        
    for i in range(weak_len):
        for di in dist_list:    #순열 중 하나 선택
            count=1             #친구 수 초기화
            position=weak[i] + di[count-1]    #현재 위치 = 취약 벽의 위치 + 투입된 친구의 이동 가능 거리
            for idx in range(i,i+weak_len):   #해당 취약지점 부터 취약지점의 거리만큼 탐색
                if position<weak[idx]:        #현재 위치가 다음 취약지점에 못미친다면
                    count+=1                  #인원을 추가 투입
                    if count > len(di):       #투입 가능한 인원이 초과했다면 반복문 종료
                        break
                    position=weak[idx]+di[count-1]    #현재 위치를 현재 취약 지점에서 새로 투입된 인원의 이동거리만큼 더함
            answer=min(answer,count)        #순열이 끝난 후 현재 투입된 최소 인원 비교
    if answer>len(dist):    #투입 인원이 초기값과 다르지 않다면 모든 지점을 이동 할 수 없는 것이므로 -1 출력
        return -1
    return answer