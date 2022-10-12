class Solution {
    boolean visited[];
    int graph[][];
    
    public int solution(int n, int[][] wires) {
        int answer = n;
        graph = new int[n][n];
        
        for (int[] wire : wires) {
            graph[wire[0]-1][wire[1]-1]=1;
            graph[wire[1]-1][wire[0]-1]=1;
        }
        
        for (int i=0;i<wires.length;i++) {
            visited = new boolean[n];
            int p1 = wires[i][0];
            int p2 = wires[i][1];
            
            visited[p2-1]=true;     //연결된 노드를 방문처리해서 끊는다.
            
            dfs(n,p1);
            int tmp = -1;           //연결된 노드까지 방문 처리를 해주었으므로, -1로 시작
            
            for (boolean v : visited) { //방문한 자식 노드의 갯수 count
                if (v) tmp++;
            }

            answer=Math.min(answer,Math.abs(tmp-(n-tmp)));  //방문한 자식과 안된 자식 구분
        }
        
        return answer;
    }
    public void dfs(int n,int node) {
        visited[node-1]=true;
        
        for (int i=0; i<n; i++) {       //연결된 자식들을 모두 방문처리
            if (graph[node-1][i]==1 && !visited[i]) {
                dfs(n,i+1);
            }
        }
    }
}
