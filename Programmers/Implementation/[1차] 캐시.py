def solution(cacheSize, cities):
    answer=0
    cache=[]
    if not cacheSize:   #cacheSize가 0일 경우
        answer=5*len(cities)
    else:
        for city in cities:
            if city.lower() in cache:   #cache hit인 경우
                answer+=1
                cache.append(cache.pop(cache.index(city.lower())))  #가장 마지막에 사용
            else:   #cache miss인 경우
                answer+=5
                if len(cache) == cacheSize:   #cache가 가득 찬 경우
                    cache.pop(0)    #사용된지 가장 오래된 도시 pop
                cache.append(city.lower())
    return answer
