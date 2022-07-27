from itertools import combinations

def solution(relation):
  
    def find_key(ke):   #ke ( ex) [1,3] 과 같은 key가 될 index 번호)를 갖고 중복 검사 여부 판단
        tmp_answer = []
        for i in range(len(relation)):
            tmp = []
            for k in ke:
                tmp.append(relation[i][k])
            if tmp not in tmp_answer:
                tmp_answer.append(tmp)
        if len(relation) == len(tmp_answer):
            return ke
        return 0
          
    answer = []
    key_num = [i for i in range(len(relation[0]))]
    
    for k in range(1,len(relation[0])+1): #후보키의 갯수를 최소1개부터 최대 col의 갯수만큼 생성
        for key in combinations(key_num,k):
            get_key = find_key(key)
            if get_key: #중복 검사 여부를 통과여부 판단
                flag = 0
                for i in range(1,len(get_key)): #만약 키중에 이미 후보키가 된 키가 들어가있을 경우 최소성 위반여부 판단
                    for gk in combinations(get_key,i):
                        print(gk,get_key)
                        if gk in answer:
                            flag = 1
                            break
                    if flag:
                        break
                if not flag:  #후보키의 조건을 갖추었으면 answer에 추가
                    answer.append(get_key)   
    return len(answer)  #후보키의 조건을 갖춘 index 갯수 반환
