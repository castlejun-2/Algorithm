#배열에서 해당 값이 삽입될 때 갖는 index를 찾아준다.
from bisect import bisect_left, bisect_right    

def counting(arr,left_val,right_val):   #정렬된 배열에서 해당 arr을 삽입 했을 때 들어가게 될 위치를 통해 사이에 몇개의 값이 들어있는지 계산
    right_idx=bisect_right(arr,right_val)
    left_idx=bisect_left(arr,left_val)
    return right_idx-left_idx

def solution(words, queries):
    array=[[] for _ in range(10001)]
    reversed_array=[[] for _ in range(10001)]
    answer = []
    for word in words:  #길이별로 문자열을 저장한다.
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])    #앞에 ?가 들어올 수 있으므로 뒤집어서 문자열을 저장한다.
    
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
        
    for que in queries:
        if que[0] == '?':   #앞에 ?가 존재한다면 뒤집어진 문자열을 응용하여 ??문자열의 갯수를 계산하여준다.
            response=counting(reversed_array[len(que)],que[::-1].replace('?','a'),que[::-1].replace('?','z'))
        else:
            response=counting(array[len(que)],que.replace('?','a'),que.replace('?','z'))
        answer.append(response)
    
    return answer