class Solution {
    static int answer = 0;
    boolean visited[];
    static int num;
    
    public int solution(int k, int[][] dungeons) {
        num = dungeons.length;
        visited = new boolean[num];
        
        recursion(dungeons,k,0,0);
        
        return answer;
    }
    public void recursion(int[][] dungeons, int health, int idx, int cnt) {     //던전을 여러 순서대로 돌아본 후 최대 갯수를 return
        answer=Math.max(answer,cnt);
        
        for (int i=0; i<num; i++) { 
            if (!visited[i] && health>=dungeons[i][0]) {
                visited[i]=true;
                recursion(dungeons,health-dungeons[i][1],idx+1,cnt+1);
                visited[i]=false;
            }
        }
    }
}
