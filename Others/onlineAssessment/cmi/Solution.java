
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;

// public class Solution {
    // public int[] solution(int N, String artifacts, String searched){
    //     int[] sol = {0,0};
    //     int count = 0, totalArtifactCells = 0; //totalArtifactCells stores the count of total number of cells an artifact occupies, count is to count the hits in search string.
    //     String[] arrOfArtifacts = artifacts.split(",", (N*N)); //Total number of artifacts.
    //     String[] eachArtifact; //Co-ordinates of artifact.
      
    //     for(int i=0;i<arrOfArtifacts.length;i++){
    //         eachArtifact = arrOfArtifacts[i].split(" ",N); //Co-ordinates of current artifact stored in array.
    //         count = 0;
    //         totalArtifactCells = 0;
          
    //         for(char j = eachArtifact[0].charAt(0); j<=eachArtifact[1].charAt(0); j++){
    //             for(char k = eachArtifact[0].charAt(1); k<=eachArtifact[1].charAt(1); k++){
    //                 totalArtifactCells++;
    //                 if(searched.contains(""+j+k)){
    //                     count++;
    //                 }
    //             }
    //         }
          
    //         if(totalArtifactCells>4){
    //             System.out.println("Artifacts should not be greater than 4 cells."); //Print error if an artifact occupies more than 4 cells.
    //             System.exit(0);
    //         }
          
    //         if(count == totalArtifactCells){
    //             sol[0]++; //increment if all cells of current artifact is found.
    //         }
    //         else {
    //             if(count!=0){
    //                 sol[1]++; //increment if not all but some are found.
    //             }
    //         }
    //     }
      
    //     return sol;
    // }

//     public static void main(String []args){
//         int[] sol = new int[2];
//         int N;
//         String artifacts, searched;
//         // SearchArtifacts SA = new SearchArtifacts();
//         Solution s = new Solution();


//         // modify below values of N, artifacts and searched before passing them to the function solution().
//         N = 4;
//         artifacts = "1B 2C,2D 4D"; // "1A 1B,2C 2C";
//         searched = "2B 2D 3D 4D 4A"; // "1B";
       
//         if(N>26||N<1){
//              System.out.println("N should be between 1 and 26.");
//              System.exit(0);
//         }
       
//         sol = s.solution(N,artifacts,searched);
//         System.out.println("Solution : [" + sol[0] + "," + sol[1] + "]."); //Print Result
//     }

// }






public class Solution {
    public int[] solution(int N, String artifacts, String searched){
        int[] res = {0,0};

        // construct hashset for constant looking up searched cells
        Set<String> set = new HashSet<String>(Arrays.asList(searched.split(" ")));

        for (String artifact : artifacts.split(",", N * N)) {
            // System.out.print("artifact: ");
            // System.out.println(artifact);
            String[] coords = artifact.split(" ");
            int artifactCnt = 0; 
            int cnt = 0; // partialConstructCnt

            String row0 = coords[0].substring(0, coords[0].length() - 1);
            String row1 = coords[1].substring(0, coords[1].length() - 1);
            for (int i = Integer.parseInt(row0); i <= Integer.parseInt(row1); ++i) {
                int X = coords[0].length(), Y = coords[1].length();

                for (char j = coords[0].charAt(X - 1); j <= coords[1].charAt(Y - 1); ++j) {
                    String tmp = "" + Integer.toString(i) + j;
                    // System.out.print(tmp);
                    artifactCnt += 1;
                    if (set.contains(tmp))
                        cnt += 1;
                }
            }

            // System.out.print("artifact: ");
            // System.out.println(artifact);
            
            // System.out.print("artifactCnt: ");
            // System.out.print(artifactCnt);
            // System.out.print(", cnt: ");
            // System.out.println(cnt);

            if (artifactCnt == cnt) {
                // found all pieces of artifacts
                res[0] += 1;
            } else if (artifactCnt != cnt && cnt != 0) {
                res[1] += 1;
            }
        }

        return res;
    }

    public static void main(String []args){
        int[] sol = new int[2];
        int N;
        String artifacts, searched;
        // SearchArtifacts SA = new SearchArtifacts();
        Solution s = new Solution();


        // modify below values of N, artifacts and searched before passing them to the function solution().
        N = 13;
        artifacts = "1A 2A,12A 12A"; // "1B 2C,2D 4D";
        searched = "12A"; // "2B 2D 3D 4D 4A";
       
        if(N>26||N<1){
             System.out.println("N should be between 1 and 26.");
             System.exit(0);
        }
       
        sol = s.solution(N,artifacts,searched);
        System.out.println("Solution : [" + sol[0] + "," + sol[1] + "]."); //Print Result
    }

}