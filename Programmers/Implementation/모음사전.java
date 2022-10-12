class Solution {
    public int solution(String word) {
        int rating[] = {781,156,31,6,1};    //각 자릿수 증가율
        String arr = "AEIOU";
        int answer = word.length();

        for (int i=0; i<word.length(); i++) 
            answer+=rating[i]*arr.indexOf(word.charAt(i));  //모음 순서에서, 각 자릿수의 위치와 증가율만큼 더해준다.

        return answer;
    }
}
