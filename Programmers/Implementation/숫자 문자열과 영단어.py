def solution(s):
    answer=[]
    dictionary={ 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    idx=0
    while idx<len(s): #s의 길이만큼탐색
        if '0'<=s[idx]<='9':  #숫자라면 answer에 바로 저장
            answer.append(s[idx])
            idx+=1
        else:
            tmp=""
            while idx<len(s) and 'a'<=s[idx]<='z' and tmp not in dictionary:  #숫자로 바뀌거나, 단어가 완성될때까지 반복
                tmp+=s[idx]
                idx+=1
            answer.append(dictionary[tmp])  #완성된 단어 tmp를 숫자로 변환해서 answer에 저장
    return int("".join(map(str,answer)))  #join함수를 통해 문자열들을 이어붙히고 int형으로 변환
