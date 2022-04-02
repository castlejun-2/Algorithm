int main(){
  string str="",tokennum="";
  int sum=0;
  bool state=false;
  cin >> str;
  
  for(int i=0;i<=str.size();i++){
    if(str[i]=='+' || str[i]=='-' || str[i]=='\0'){                         //연산자를 만났을 때
      if(state){                                                            //minus 상태라면 모아둔 토큰값(tokennum)을 빼준다
        sum-=stoi(tokennum);
        tokennum="";
      }
      else{                                                                 //minus 상태가 아니라면 토큰값(tokennum)을 더해준다
        sum+=stoi(tokennum);
        tokennum="";
      }
      if(str[i]=='-'){                                                      //'-'연산자를 만난다면 minus 상태로 들어가게 된다
        state=true;
        continue;                                                           //stoi를 할 때 -가 tokennum에 들어간다면 음수로 인식됨으로 continue 사용
      }
    }  
    tokennum+=str[i];                                                       //피연산자들의 string들은 더해주면서 token을 형성해준다
  }
  cout << sum << endl;                                                    
  return 0;
}  
