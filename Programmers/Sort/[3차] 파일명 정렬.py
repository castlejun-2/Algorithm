import re

def solution(files):
    tmp_answer = []
    answer = []
    for i in range(len(files)):
        startNumIdx=re.search('[0-9]',files[i]).start()
        startTailIdx=startNumIdx+1
        head=files[i][:startNumIdx]
        flag=0
        for k in range(startNumIdx+1,len(files[i])):
            if not files[i][k].isdigit():
                startTailIdx=k
                flag=1
                break
        if not flag:    #꼬리가 없는 경우
            number=files[i][startNumIdx:]
            tail=""
        else:           #꼬리가 있는 경우
            number=files[i][startNumIdx:startTailIdx]
            tail=files[i][startTailIdx:]
        tmp_answer.append([head,number,tail,i])
    tmp_answer.sort(key=lambda x:(x[0].lower(),int(x[1]),x[3])) #대소문자 제거, int형 변환, 입력 순으로 정렬
    for tmp in tmp_answer:
        answer.append("".join(map(str,tmp[:3])))    #join을 통한 문자열 입력
    return answer
