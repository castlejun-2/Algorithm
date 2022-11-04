import re

def solution(skill, skill_trees):
    answer = 0
    ans={}
    for j in range(1,len(skill)+1): #가능한 조합 생성
        ans[skill[:j]]=1

    for tree in skill_trees:        
        n_tree=re.sub("[^"+skill+"]","",tree) #skill을 제외한 다른 문자는 제거

        if n_tree in ans or not n_tree:       #제거된 문자열이 가능한 조합 순서에 있거나, 비어 있다면 가능한 조합
            answer+=1
    return answer
