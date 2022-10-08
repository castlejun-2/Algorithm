import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        int N = maps.length;
        int M = maps[0].length;
        int dx[] = {0,0,-1,1};
        int dy[] = {1,-1,0,0};
        boolean visited[][] = new boolean[N][M];
        Queue<Node> q = new LinkedList<>();
        q.add(new Node(0,0,1));

        while (!q.isEmpty()) {
            Node node = q.poll();
            if (node.x==N-1 && node.y==M-1){    //도착지에 도착했다면, 최단거리로 도착한것이므로 바로 return
                return node.point;
            }
            
            for (int i=0;i<4;i++){        //bfs를 통해 동서남북 탐색
                int nx = node.x + dx[i];
                int ny = node.y + dy[i];
                if (nx >= 0 && ny >= 0 && nx < N && ny < M) {
                    if (maps[nx][ny]==1 && !visited[nx][ny]){   //길이 뚫려있고 방문하지 않았다면, 탐색
                        visited[nx][ny]=true;
                        q.add(new Node(nx,ny,node.point+1));    //길이를 +1 해준다.
                    }
                }
            }
        }
        
        return -1;
    }
    public class Node {
        int x;
        int y;
        int point;
        
        public Node(int x, int y, int point) {
            this.x = x;
            this.y = y;
            this.point = point;
        }
    }
}
