//Agilan Ampigaipathar (100553054)
public class Main {
	
	public static int editDistance(String firstWord, String compareWord) {
		//Initiate the tables 
		int distance[][] = new int[firstWord.length()+1][];

		for (int i = 0; i < distance.length; i++) {
			distance[i] = new int[compareWord.length()+1];
			for (int j = 0; j < distance[i].length; j++) {
				distance[i][j] = 0;
			}
		}
		
		//Deletes away from empty string
		for (int i = 0; i < distance.length; i++) {
			distance[i][0] = i;
		}
		
		//Inserts away from empty string
		for (int j = 0; j < distance[0].length; j++) {
			distance[0][j] = j;
		}
    
		for (int j = 1; j <= compareWord.length(); j++) {
			for (int i = 1; i <= firstWord.length(); i++) {
				if (firstWord.charAt(i-1) == compareWord.charAt(j-1)) {
          // Characters already match
					distance[i][j] = distance[i-1][j-1];
				}
        //Minimum  
        else {
          //Deletion 
					int delete = distance[i-1][j] + 1;
          //Insertion 
					int insert = distance[i][j-1] + 1;
          //Substitution
					int subst  = distance[i-1][j-1] + 1;

					distance[i][j] = minimum(delete, insert, subst);
				}
			}
		}



		return distance[firstWord.length()][compareWord.length()];
	}

    //Figure out minimum
  	public static int minimum(int n1, int n2, int n3) {
      if (n1 < n2) {
        if (n1 < n3) {
          return n1; 
        }
        else {
          return n3;
        } 
      }
      if (n2 < n3) {
        return n2;
      }
      else {
        return n3;
      }
	}
	
	public static void main(String[] args) {
    //Test cases 
		String word1 = "spoof";
		String word2 = "stool";
    String word3 = "podiatrist";
		String word4 = "pediatrician";
    String word5 = "blaming";
		String word6 = "conning";

    int result1 = editDistance(word1, word2);
    int result2 = editDistance(word3, word4);
    int result3 = editDistance(word5, word6);

		System.out.println("The minimum edit distance between '"+ word1 +"' and '"+ word2 +"' is " + result1);

    System.out.println("The minimum edit distance between '"+ word3 +"' and '"+ word4 +"' is " + result2);

    System.out.println("The minimum edit distance between '"+ word5 +"' and '"+ word6 +"' is " + result3);
	}
}