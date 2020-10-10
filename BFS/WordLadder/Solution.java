import java.util.*;

class Solution {

    // beginWord.length() = M, wordLise.size() = N
    // M * M * N = O(M^2 * N)
    public int ladderLength(String beginWord, String endWord,   List<String> wordList) {
        if (wordList.isEmpty()) {
            return beginWord.equals(endWord) ? 1 : 0;
        }
        
        Queue<String> queue = new LinkedList<>();
        Set<String> words = new HashSet<>(wordList);
        queue.offer(beginWord);
        int level = 1;
        
        while (!queue.isEmpty()) {
            int N = queue.size();
            for (int i = 0; i < N; ++i) {
                String curWord = queue.poll();
                // Find next word
                char[] curWordChars = curWord.toCharArray();
                for (int j = 0; j < curWordChars.length; ++j) {
                    for (char k = 'a'; k <= 'z'; ++k) {
                        char tmp = curWordChars[j];
                        curWordChars[j] = k;
                        String nextWord = new String(curWordChars);
                        if (words.contains(nextWord)) {
                            
                            if (nextWord.equals(endWord)) {
                                return level + 1;
                            }
                            
                            queue.offer(nextWord);
                            words.remove(nextWord); 
                        }
                        
                        curWordChars[j] = tmp;
                    }
                }
            }// for
            level++;
        }//while
        
        return 0;
    }

    public static void main(String[] args) {
        System.out.println("Thsi is wordladder");
    }
}


/*

aot    
bot
.
dot -> 
.
zot

*/