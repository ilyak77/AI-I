import java.util.*;
import java.io.*;


public class guess_b{
	public static void main(String[] args) {
		String filePath = "file5.txt";
		ArrayList<String> word = new ArrayList<String>();
		ArrayList<Integer> count = new ArrayList<Integer>();
		ArrayList<Float> prob = new ArrayList<Float>();
		Map<String,Integer> hm = new HashMap<>();
		int sum = 0;

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
                hm.put(part[0],count_temp);
            }   

            PriorityQueue<Map.Entry<String,Integer>> pq = new PriorityQueue<Map.Entry<String,Integer>>
		       (new Comparator<Map.Entry<String,Integer>>(){
                  public int compare(Map.Entry<String,Integer> a, Map.Entry<String,Integer> b){
             	     return b.getValue() - a.getValue();
                  }
		    });

		    for(Map.Entry<String,Integer> entry: hm.entrySet()){
               pq.offer(entry);

               if(pq.size()>10){
            	 pq.poll();
               }
		    }

		    for(Map.Entry<String,Integer> entry:pq){
		    	System.out.println(entry.getKey()+", "+ (float)entry.getValue()/sum);
		    }


        
        }
        catch(FileNotFoundException ex) {
            System.out.println( "Unable to open file");                
        }
        catch(IOException ex) {
            System.out.println("Error reading file");                  
        }
	}
}