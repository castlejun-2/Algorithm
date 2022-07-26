from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer=[]
    dic={}
    for i in info:
        tmp=i.split(' ')
        spec=tmp[:-1]
        score=tmp[-1]
        
        for i in range(5):  #이 때 java를 배운다면 -(=상관없음) 일때도 가능하므로 가능한 조합 생성
            for comb in combinations(spec,i):   #ex) javabackendjuniorpizza = [50,20] 등의 해쉬 생성
                dicIdx="".join(comb)    
                if dicIdx not in dic:   
                    dic[dicIdx]=[int(score)]
                else:
                    dic[dicIdx].append(int(score))
    
    for d in dic:   #점수순으로 dictionary 정렬
        dic[d].sort()
        
    for qe in query:
        tmp=qe.replace('-','').split(' and ')   #-를 제거 후 and로 list 구분
        key,score="".join(tmp).split(' ')   #공백을 기준으로 key와 점수로 구분
        cnt=0
        if key in dic:  #해당 키가 이 전의 dic에 존재한다면
            if dic[key]:
                cnt=bisect_left(dic[key],int(score))    #score의 index를 찾아
                answer.append(len(dic[key])-cnt)        #len(dic[key])-cnt를 해주면 score 점수 이상의 갯수
        else:   #key가 존재하지 않을 경우
            answer.append(0)    
    return answer
