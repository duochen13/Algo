import java.util.*;

class Solution {

    public List<List<String>> groupAnagrams(String[] strs) {
        
        Map<String, List> memo = new HashMap<>();
        
        for (String str : strs) {
            char[] tmp = str.toCharArray();
            Arrays.sort(tmp);
            String key = new String(tmp);
            if (!memo.containsKey(key)) {
                memo.put(key, new ArrayList<String>());
            } 
            memo.get(key).add(str);
        }
        
    return new ArrayList(memo.values());
    

}
