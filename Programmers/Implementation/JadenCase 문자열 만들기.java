class Solution {
    public String solution(String s) {
        String arr[] = s.toLowerCase().split("");       //각 값을 문자열배열로 저장
        boolean flag = true;
        String answer = "";
        
        for (String tmp : arr) {
            answer += flag ? tmp.toUpperCase() : tmp;   //앞에 공백이였다면 대문자로 변경, 그렇지 않다면 원래 값 유지
            flag = tmp.equals(" ") ? true : false;      //현재 값이 공백이면 flag를 True, 그렇지 않다면 False로 설정
        }
        
        return answer;
    }
}
