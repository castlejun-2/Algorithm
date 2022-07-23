from itertools import combinations

def solution(orders, course):
    answer = []
    number = [0]*20
    array = [[] for _ in range(20)]
    courses = {}
    for order in orders:
        menu=[]
        order=list(order)
        order.sort()
        for i in range(2,len(order)+1): #각 단품메뉴에서 생성되는 메뉴의 조합
            menu+=list(combinations(order,i))
        for me in menu: #생성된 메뉴의 조합 count
            if "".join(map(str,me)) not in courses:
                courses["".join(map(str,me))]=1
            else:
                courses["".join(map(str,me))]+=1
    for key,value in courses.items(): #생성된 메뉴의 조합중에서 같은 길이중 가장 많이 언급된 조합 탐색
        if value > 1:
            if not number[len(key)-1]:
                array[len(key)-1].append(key)
                number[len(key)-1]=value
            elif number[len(key)-1] < value:  #현재의 key일 때 최댓값이라면
                number[len(key)-1]=value  #최댓값 갱신
                array[len(key)-1].clear() #이 전의 값들은 삭제
                array[len(key)-1].append(key) #새로 생성된 최댓값 추가
            elif number[len(key)-1] == value: #최대값과 값이 같다면 값 추가
                array[len(key)-1].append(key)
    for i in course:  #course에 나온 길이들의 값을 answer에 추가
        answer+=array[i-1]
    answer.sort() #사전순으로 정렬
    return answer
