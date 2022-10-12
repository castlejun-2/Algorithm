import java.util.*;

class Solution {
    public int solution(int[][] routes) {
        Arrays.sort(routes,(int s1[], int s2[])->s1[1]-s2[1]);  //도착 시간 기준 오름차순 정렬
        int answer = 0;
        int last = routes[0][1];
        
        for (int i=1; i<routes.length; i++){
            if (routes[i][0]<=last) answer++;   //시작시점이, 이 전 차량의 도착지점보다 이 전이라면 동일 범위 내에 존재
            else last=routes[i][1];             //그렇지 않다면 끝 지점 변경
        }
        
        return routes.length-answer;            //동일 범위에 있는 차량의 갯수를 빼준다.
    }
}
