import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        HashMap<String,Integer> genre = new HashMap<>();      //장르의 총 앨범 판매량 저장
        HashMap<String,HashMap<Integer,Integer>> music = new HashMap<>();   //장르별 곡들의 정보 저장
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int i=0;i<genres.length;i++) {
            if (!music.containsKey(genres[i])) {
                HashMap<Integer, Integer> map = new HashMap<>();
                map.put(i,plays[i]);  
                music.put(genres[i],map);                     //장르를 생성하고, 앨범 정보 입력
            } else 
                music.get(genres[i]).put(i,plays[i]);         //이미 장르가 있다면, 장르에 새로운 앨범 정보 입력
            genre.put(genres[i],genre.getOrDefault(genres[i],0)+plays[i]);
        }
        
        List<String> gr = new ArrayList(genre.keySet());
        Collections.sort(gr, (s1, s2) -> genre.get(s2) - genre.get(s1));    //장르별 앨범 판매량 순으로 정렬된 장르의 key 값 배열
        
        for (String g : gr) {
            HashMap<Integer, Integer> map = music.get(g);         //g 장르의 앨범 정보들을 map 변수에 저장
            List<Integer> gk = new ArrayList(map.keySet());       //앨범의 고유번호를 가져온다
            Collections.sort(gk, (s1,s2) -> map.get(s2) - map.get(s1));     //고유 번호를, 앨범 판매량 순으로 정렬
            
            for (int k=0; k<2 && k<gk.size(); k++){               //최대 두장까지 앨범 정보 입력
                answer.add(gk.get(k));
            }   
        }
        
        return answer.stream().mapToInt(i->i).toArray();      //Array배열을 int 배열로 변환
    }
}
