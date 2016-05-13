import java.util.*;
import java.io.*;


public class guess{

	public static void main(String[] args) {
		String filePath = "file5.txt";
		int sum = 0;

    ArrayList<String> word = new ArrayList<>();
    ArrayList<Integer> count = new ArrayList<>();
    ArrayList<Float> prob = new ArrayList<>();

		 try {
            FileReader file = new FileReader(filePath);
            BufferedReader buffer = new BufferedReader(file);
            String line;

            while((line = buffer.readLine()) != null){
                String[] part = line.split(" ");
                word.add(part[0]);
                int count_temp = Integer.parseInt(part[1]);
                sum += count_temp;
                count.add(count_temp);

            }   

            System.out.println("sum: "+sum);

            for(int i = 0; i<word.size(); i++){
              float probility = (float)count.get(i)/sum;
              prob.add(probility);
            }
        
        }
      catch(FileNotFoundException ex) {
            System.out.println( "Unable to open file");                
      }
      catch(IOException ex) {
            System.out.println("Error reading file");                  
      }
       
      HashSet<Character> p1 = new HashSet<>();
      String s1 = "D**I*";
      //p1.add('A');
      //p1.add('E');
      //p1.add('M');
      //p1.add('N');
      //p1.add('T');
      bestGuess(s1,p1,word,prob);

      System.out.println("the letter "+ ch+", the probility is "+f);
  }




  public static void bestGuess(String correctGuess, HashSet<Character> wrongGuess, ArrayList<String> word, ArrayList<Float> prob){
    float[] lguess = new float[26];
    ArrayList<Integer> tag = new ArrayList<>();
    float sumProb = 0;

    for(int i = 0; i< word.size();i++){
      String w = word.get(i);
      boolean check = true;

      for(int j = 0; j<5 ;j++){
        if((correctGuess.charAt(j) =='*' && contains(correctGuess, w.charAt(j))) || (correctGuess.charAt(j)!='*' && correctGuess.charAt(j)!= w.charAt(j))){
          check = false;
          break;
        }else if(wrongGuess.contains(w.charAt(j))){
          check = false;
          break;
        }

      }

      if(check){
        tag.add(1);
        sumProb += prob.get(i);

      }else{
        tag.add(0);
      }
    }

    System.out.println("sum of prob = "+sumProb);

    for(int i = 0; i<word.size();i++){
      if(tag.get(i)==0) continue;

      float p = (prob.get(i))/sumProb;
      for(int l = 0; l <26; l++){
        char temp = (char)('A'+l);
        if(!contains(correctGuess,temp) && !wrongGuess.contains(temp) && contains(word.get(i),temp)){
          lguess[l] += p;
        }
      }

    }
    
    float maxP = 0;
    char bestL = '\n';

    for(int i = 0; i<26; i++){
      if(maxP < lguess[i]){
        maxP = lguess[i];
        bestL = (char)('A'+i);
      }
    }
   
    ch = bestL;
    f = maxP;

  }

  private static char ch = '\n';
  private static float f = 0;

   private static boolean contains(String s, char c){
     for(int i = 0; i< s.length();i++){
       if(s.charAt(i) ==c) return true;
     }
     return false;
   }


}
