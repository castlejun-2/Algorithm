from collections import defaultdict

def solution(gems):
    _dict = defaultdict(lambda: 0)
    _len_gems = len(gems); _len_keys = len(set(gems))
    answer = [0, 100001]
    start = 0; end = 0;

    while start < _len_gems:                       #시작점이 끝까지 도달했다면 탐색 종료
        _len = len(_dict)
        if _len == _len_keys:
            _dict[gems[start]] -= 1
            if _dict[gems[start]] == 0:
                del _dict[gems[start]]
            start += 1
            if answer[1]-answer[0] > end - start:   #구간이 짧아지면 갱신 (같은 경우 제외: 같을 경우 start가 작은 것을 return 함으로)
                answer = [start,end]
            continue
        if end == _len_gems:                        #끝점에 도달했다면 종료 (이때, end가 끝점을 넘어도 앞의 start를 줄여 구간을 줄일 수 있으므로 start 확인 이후에 위치
            break
        if _len != _len_keys:                       #보석을 다 훔치지 못하였다면 끝점 포인터 먼저 이동
            _dict[gems[end]] +=1
            end += 1
    return answer
