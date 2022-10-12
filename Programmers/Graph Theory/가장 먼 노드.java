import java.util.*;

class Solution {
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();   // key: List를 갖는 배열 생성
    static int[] visited;
    
    public int solution(int n, int[][] edge) {
        visited = new int[n];
        int answer = 0;
        
        for (int i=0; i<n; i++){
            graph.add(i, new ArrayList<>());
        }
        
        for (int[] e : edge) {                //각 노드에, 연결된 노드 값 추가
            graph.get(e[0]-1).add(e[1]-1);    
            graph.get(e[1]-1).add(e[0]-1);
        }
        
        bfs(0,n);

        int max = Arrays.stream(visited).max().getAsInt();  //최대값 탐색
        
        for (int k : visited)           //최대값과 같은 노드의 갯수 탐색
            if (k==max) answer++;
        
        return answer; 
    }
    public void bfs(int idx,int n) {
        Queue<Node> q = new LinkedList<>();
        q.add(new Node(idx,1));
        visited[idx]=1;
        
        while (!q.isEmpty()) {    //연결된 노드를 방문해주며, 깊이 값을 갱신한다. (이때, 처음 접근한 깊이가 1부터 해당 노드까지의 깊이다)
            Node node = q.poll();
            
            for(int val: graph.get(node.nd)) {
                if (visited[val]==0) {
                    visited[val]=node.depth+1;
                    q.add(new Node(val,node.depth+1));
                }
            }
        }
    }
    public class Node {
        int nd;
        int depth;
        
        public Node(int n, int dp) {
            this.nd=n;
            this.depth=dp;
        }
    }
}
