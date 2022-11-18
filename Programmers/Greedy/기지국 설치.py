import math

def solution(n, stations, w):           #stations의 길이가 10,000이므로 이를 활용해 시간 복잡도를 해결한다.
    answer = 0
    start = 1
    for i in range(len(stations)):      #길이가 n인 곳에 거리가 w인 기지국의 필요 갯수는 math.ceil(n/(w*2+1)) 이다.  
        distance = stations[i]-w-start
        if distance > 0:
            answer += math.ceil(distance/(w*2+1))
        start = stations[i]+w+1
    if start <= n:                      #앞의 값과 비교하기 때문에, n과 가장 마지막 기지국은 계산이 되지 않는다.
        answer += math.ceil((n-start+1)/(w*2+1))
    return answer
