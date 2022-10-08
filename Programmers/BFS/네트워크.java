class Solution {
    public int solution(int n, int[][] computers) {
        boolean visited[] = new boolean[computers.length];
        int answer = 0;
        
        for (int i = 0; i<n; i++){          
            if (!visited[i]){               //방문하지 않았으면 방문
                dfs(i,computers,visited);   //연결된 네트워크 전부 탐색
                answer++;                   
            }
        }
        
        return answer;
    }
    void dfs(int idx,int[][] computers,boolean[] visited){
        visited[idx]=true;
        for (int i=0; i<computers.length; i++){           //연결된 네트워크 탐색
            if (computers[idx][i]==1 && !visited[i]) {    //현재 idx 네트워크와 연결되어 있고, 방문하지 않았다면 방문
                dfs(i,computers,visited);
            }
        }
    }
}
