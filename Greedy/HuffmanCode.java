package Algorithm;
import java.util.*;
import java.io.*;

public class Huffman {
	//Huffman Code에서의 각 Node
	public static class Node{
		public char ch;	//문자를 담을 변수
		public int f; //빈도수를 담을 변수
		public Node left,right; //자식노드의 왼쪽과 오른쪽을 가리키는 변수
	}
	
	//전역 변수
	public static PriorityQueue<Node> pq = new PriorityQueue<>(new Comparator<Node>() {  //우선순위 큐 변수 선언
		public int compare(Node a,Node b) { //빈도수가 오름차순으로 우선순위 큐에 정렬
				return a.f-b.f;
		}
	});
	public static HashMap<Character,String> printhuffman = new HashMap<Character,String>(); //변환된 Huffman Code를 담을 변수
	public static HashMap<Character,Integer> fq = new HashMap<Character,Integer>();	 //문자에 따른 빈도수를 저장할 변수
	
	//Huffman Tree 생성 함수
	public static Node createhuffman(int n) {
		for(int q=0;q<n-1;q++) {
			Node temp = new Node();
			temp.right = pq.poll();
			temp.left = pq.poll();
			temp.f=temp.right.f + temp.left.f; //오름차순으로 정렬된 빈도수가 작은 두개 노드의 빈도수를 더함
			pq.add(temp);					   //다시 우선순위큐에 더해진 값을 삽입
		}
		return pq.poll(); //최종적으로 남은 root Node 반환
	}
	
	//Huffman Tree 중위 순회 함수
	public static void traversal(Node Nd,String st) {
		if(Nd == null)
			return;
		traversal(Nd.left,st+"0");		//왼쪽노드로 갈때 0추가
		traversal(Nd.right,st+"1");		//오른쪽노드로 갈때 1추가
		if(Nd.ch != '\0') {				//노드의 character가 비어있지 않다면 출력
			System.out.print("\"" + Nd.ch + "\" frequency: ");
			System.out.print(fq.get(Nd.ch));
			System.out.println(" and HuffmanCode: " + st);
			printhuffman.put(Nd.ch, st);
		}
	}
	
	static public void main(String[] args) {
		
		int num=0; //전체 노드의 갯수를 확인할 변수
		Scanner sc = new Scanner(System.in);
		System.out.print("Huffman Code로 수정할 문자열: ");
		try { //test.txt 파일로부터 문자열 읽어오기
			String fstr = "C:\\Users\\LEE\\OneDrive\\Desktop\\Dankook university\\3학년\\알고리즘/test.txt";
			BufferedReader bstr = new BufferedReader(new FileReader(fstr));
			String str = bstr.readLine(); 
			System.out.println(str + "\n");
			for(int j=0;j<str.length();j++) {
				char c = str.charAt(j);
				if(fq.containsKey(c))
					fq.put(c,fq.get(c)+1); //해쉬함수에 존재하던 key 값이면 빈도수만 +1 증가
				else
					fq.put(c,1);
				}
		
			for(Character t:fq.keySet()) { //해쉬의 key 값에 맞는 value들을 가져온 후 우선순위 큐에 삽입
				Node temp = new Node();
				temp.ch=t;
				temp.f=fq.get(t);
				pq.add(temp);
				num++;
			}
			//Huffman Tree 생성 및 중위순회를 통한 값 획득
			Node root = createhuffman(num);	//root 노드 반환
			traversal(root,new String());	//root 노드부터 중위 우선순회 
		
			//Huffman Code 출력
			System.out.println("\n======Huffman Code 출력======");
			String print_result = new String();
			for(int k=0;k<str.length();k++)
				print_result = print_result + printhuffman.get(str.charAt(k)) + " ";
			System.out.println(print_result);
		}catch (Exception e) {
			e.printStackTrace();
		}
	}
}
