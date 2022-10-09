class Solution {
    public int solution(String dirs) {
        int dx[] = {-1,0,1,0};
        int dy[] = {0,1,0,-1};
        int answer = 0;
        boolean visited[][][] = new boolean[11][11][4];
        int x=5, y=5;
        
        for (int i=0;i<dirs.length();i++){
            char cmd = dirs.charAt(i);
            int d = 0;
            if (cmd=='L') d=3;
            else if (cmd=='R') d=1;
            else if (cmd=='D') d=2;
            
            int nx=x+dx[d];       //방향에 따른 nx값 측정
            int ny=y+dy[d];
            
            if (nx>=0 && nx<=10 && ny>=0 && ny<=10){
                if (!visited[x][y][d]&&!visited[nx][ny][(d+2)%4]){  //온 경로 체크 표시
                    visited[x][y][d]=true;
                    visited[nx][ny][(d+2)%4]=true;
                    answer++;
                }
                x=nx;     //현재 좌표 수정
                y=ny;
            }   
        }
        
        return answer;
    }
}
