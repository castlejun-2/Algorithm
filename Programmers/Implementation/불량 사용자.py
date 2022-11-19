from itertools import permutations

def solution(user_id, banned_id):
    def isEquals(users,ban):        #문자열이 각 banned_id에 모두 일치하는지 확인
        for i in range(len(users)):
            if len(users[i]) != len(ban[i]):
                return False
            for j in range(len(users[i])):        
                if ban[i][j]=='*' or users[i][j]==ban[i][j]:
                    continue
                return False
        return True
    answer = []
    
    for case in permutations(user_id,len(banned_id)):
        if isEquals(case,banned_id):
            if set(case) not in answer:   #순열로 인해, 순서에 관계없이 매칭하므로 중복 문자열이 생길 수 있어 이를 해결하기 위한 코드
                answer.append(set(case))
    return len(answer)
