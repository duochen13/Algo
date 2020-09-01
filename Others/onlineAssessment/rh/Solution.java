
import java.util.Set;
import java.util.HashSet;




class Solution {

    public boolean playground(String[] a, String[] b){

        boolean isPrefix = true;
        Set<String> set = new HashSet<>();

        StringBuilder tmp = new StringBuilder("");
        for (int i = 0; i< a.length; ++i) {
            tmp.append(a[i]);
            // stringbuilder -> string
            System.out.println(tmp.toString());
            set.add(tmp.toString());
        }

        for (String s : b) {
            if (!set.contains(s))
                return false;
        }

        return true;
    }

    public static void main(String[] arg) {
        Solution s = new Solution();
        String[] a = new String[]{"apple","pie","pineapple"};
        String[] b = new String[]{"applepie", "pineapplepie"};
        boolean res = s.playground(a, b);

        System.out.println(res);
    }
}