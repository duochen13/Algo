
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

    public int divideSubstring(int n, int k) {
        // assert k > 0
        // generate all substring combinations with length k
        String digits = Integer.toString(n);
        Set<String> set = new HashSet<String>();
        // int res = 0;

        for (int i = 0; i <= digits.length() - k; ++i) {
            String tmp = digits.substring(i, i + k);
            int tmpNum = Integer.parseInt(tmp);
            if (n % tmpNum == 0) {
                set.add(tmp);
            }
        }
        return set.size();
    }

    public int difference(int[] a, int[] b) {
        int res = 0;
        int N = a.length;
        for (int i = 0; i < N; ++i) {
            res += Math.abs(a[i] - b[i]);
        }
        return res;
    }
    public int minDifference(int[] a, int[] b) {
        // assert(a.length() == b.length())
        int N = a.length;
        int res = difference(a, b);

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (i == j)
                    continue;
                a[i] = a[j];
                res = Math.min(res, difference(a, b));
                System.out.println(res);
            }
        }

        return res;
    }

    public static void main(String[] arg) {
        Solution s = new Solution();

        int[] a = new int[]{1,3,5};
        int[] b = new int[]{5,3,1};
        int res = s.minDifference(a, b);

        System.out.println(res);
        
        // int n = 5341, k = 2;
        // int res = s.divideSubstring(n, k);
        // System.out.println(res);

        // String[] a = new String[]{"apple","pie","pineapple"};
        // String[] b = new String[]{"applepie", "pineapplepie"};
        // boolean res = s.playground(a, b);
        // System.out.println(res);
    }
}