class Solution {
    public int solution(int[][] sizes) {
        int answer=0;
        int width=0,height=0;
        
        for (int i=0;i<sizes.length; i++){
            if (sizes[i][0]<sizes[i][1]){ //세로가 더 길면 가로로 변환(=모든 지갑을 눕힌다)
                int tmp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = tmp;
            }
            if (width<sizes[i][0]) width=sizes[i][0];
            if (height<sizes[i][1]) height=sizes[i][1];
        }
        
        return width*height;
    }
}
