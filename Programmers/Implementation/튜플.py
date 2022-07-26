def solution(s):
    answer = []
    arr = s[2:len(s)-2].split("},{")  #"},{"를 기준으로 문자열을 split
    arr.sort(key=len) #문자열의 길이를 기준으로 문자열 split
    
    for a in arr:
        for i in a.split(','):  #구분된 문자열에서 ,를 기준으로 한번 더 split
            if i.isdecimal() and not int(i) in answer:  #i가 숫자이고, answer에 포함되어 있지않다면 추가
                answer.append(int(i))
    return answer #4번 line에서 length를 기준으로 정렬하였으므로, 튜플이 올바르게 정렬되어 있다.
