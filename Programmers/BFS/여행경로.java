import java.util.*;

class Solution {
    boolean visited[];
    ArrayList<String> ansRoute = new ArrayList<>();
    
    public String[] solution(String[][] tickets) {
        HashMap<String,ArrayList<String>> map = new HashMap<>();
        visited = new boolean[tickets.length];
        String[] answer = {};
        
        Arrays.sort(tickets, (s1, s2) -> {      //2차원 배열의 앞의 값 기준 정렬(같을 시 뒤의값 오름차순 정렬)
            if (s1[0].equals(s2[0]))
                return s1[1].compareTo(s2[1]);
            return s1[0].compareTo(s2[0]);
        });
        
        dfs("ICN","ICN",tickets,0);             //ICN 부터 출발
        
        return ansRoute.get(0).split(" ");      //오름차순으로 정렬되어 dfs를 했으므로, 가장 앞의 값 반환
    }
    public void dfs(String start, String route, String[][] tickets, int cnt) {
        if (cnt==tickets.length) {              //모든 ticket을 탐색 하였을 경우 값 비교
            ansRoute.add(route);
            return;
        }
        
        for (int i=0; i<tickets.length; i++) {
            if (start.equals(tickets[i][0]) && !visited[i]){    //출발점과 같고, 사용하지 않은 티켓 이라면
                visited[i]=true;
                dfs(tickets[i][1],route+" "+tickets[i][1],tickets,cnt+1);
                visited[i]=false;
            }
        }
    }
}
