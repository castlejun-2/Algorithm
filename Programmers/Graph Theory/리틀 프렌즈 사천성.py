import java.util.*;

class Solution {
    public String solution(int m, int n, String[] board) {
        String answer = "";
        boolean flag = false;
        while (true) {
            flag = false;
            String tmp = "";
            List<int []> idx = new ArrayList<>();
            for (int i=0; i<m; i++) {
                for (int j=0; j<n; j++) {
                    if (board[i].charAt(j) == '.' || board[i].charAt(j) == '*')
                        continue;
                    for (int k=j+1; k<n; k++) {   //같은 라인에 존재하는지 확인
                        if (board[i].charAt(k) == board[i].charAt(j)) {
                            tmp += board[i].charAt(j);
                            idx.add(new int[]{i,k});
                            idx.add(new int[]{i,j});
                            flag = true;
                        } else if (board[i].charAt(k) == '.' || board[i].charAt(k) == '*') {
                            for (int t=i+1; t<m; t++) { //한번 꺾인 수직에 있는지 존재 확인
                                if (board[i].charAt(j) == board[t].charAt(k)) {
                                    tmp += board[i].charAt(j);
                                    idx.add(new int[]{t,k});
                                    idx.add(new int[]{i,j});
                                    flag = true;
                                } else if (board[t].charAt(k) == '.' || board[t].charAt(k) == '*')
                                    continue;
                                break;
                            }
                            continue;
                        }
                        break;
                    }
                    for (int k=j-1; k>-1; k--) {   //같은 라인에 존재하는지 확인
                        if (board[i].charAt(k) == '.' || board[i].charAt(k) == '*') {
                            for (int t=i+1; t<m; t++) { //한번 꺾인 수직에 있는지 존재 확인
                                if (board[i].charAt(j) == board[t].charAt(k)) {
                                    tmp += board[i].charAt(j);
                                    idx.add(new int[]{t,k});
                                    idx.add(new int[]{i,j});
                                    flag = true;
                                } else if (board[t].charAt(k) == '.' || board[t].charAt(k) == '*')
                                    continue;
                                break;
                            }
                            continue;
                        }
                        break;
                    }
                    for (int t=i+1; t<m; t++) {
                        if (board[i].charAt(j) == board[t].charAt(j)) {
                            tmp += board[i].charAt(j);
                            idx.add(new int[]{t,j});
                            idx.add(new int[]{i,j});
                            flag = true;
                        } else if (board[t].charAt(j) == '.' || board[t].charAt(j) == '*')
                            continue;
                        break;
                    }
                }
            }
            if (!flag) {
                break;
            }
            for (int[] id : idx)
                board[id[0]] = board[id[0]].replace(String.valueOf(board[id[0]].charAt(id[1])),".");
            tmp = tmp.replace(".","");
            char[] ans = tmp.toCharArray();
            Arrays.sort(ans);
            String as = new String(ans);
            answer += as;
        }
        for (int i=0; i<m; i++) {
            if (board[i].replaceAll("[*.]","").length() == 0)
                continue;
            return "IMPOSSIBLE";
        }
        return answer;
    }
}
