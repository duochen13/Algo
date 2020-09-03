

class Solution {

    // time worse case: O(m + n), space: O(m)
    // T: aaaaaaaaaaaaab
    // P:    aaaaaaab
    // genera idea:
    // 1. preprocessing: build table: O(m)
    // 2. matching: O(n)

    // T: a b a a c a b a b c a c

    // P: a b a b c
    // prefix table: 
    // -1
    // 0  a
    // 0  a b
    // 1  a b a
    // 2  a b a b  len(2) maxprefix: aba, maxpostfix: bab    len(3) ab, ab
    // 0  a b a b c

    // prefix table
    // a b a b c
    //-1 0 0 1 2 

    public int[] kmp(String T, String P) {
        int[] res = new int[2];

        // construct prefix table from string P
        int[] prefix = new int[P.length()];
        prefix[0] = -1;
        int i = 0;
        int len = 0;
        while (i < P.length()) {
            if (P.charAt(i) == P.charAt(len)) {
                ++len;
                prefix[i] = len;
                ++i;
            } else {
                if (len > 0) {
                    len = prefix[len - 1];
                }
            }
        }

        return res;
    }

    public static void main(String[] args) {
        String T = "abaacababcac";
        String P = "ababc";

        Solution s = new Solution();
        int[] res = s.kmp(T, P);

        System.out.println("hello");
    }
}