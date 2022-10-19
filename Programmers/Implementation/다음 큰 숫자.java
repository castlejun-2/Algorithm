class Solution {
    public int solution(int n) {
        int tmp = n+1;
        int answer = 0;
        while (true) {
            if (Integer.bitCount(n)==Integer.bitCount(tmp++)) { //1의 갯수가 같으면 종료
                answer=tmp;
                break;
            }
        }
        return answer-1;
    }
}
