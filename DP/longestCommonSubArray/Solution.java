class Solution {

    public int LongestContinuousCommonArray(int[] A, int[] B) {
        int m = A.length, n = B.length;
        int[][] dp = new int[m + 1][n + 1];

        int res = 0;
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (A[i] == B[j]) {
                    dp[i][j] = dp[i + 1][j + 1] + 1;
                    res = Math.max(res, dp[i][j]);
                }
            }
        }
        return res;
    }

    public int LLCCA(String[] A, String[] B) {
        int m = A.length, n = B.length;
        int[][] dp = new int[m + 1][n + 1];

        int res = 0;
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (A[i].equals(B[j])) {
                    dp[i][j] = dp[i + 1][j + 1] + 1;
                    res = Math.max(res, dp[i][j]);
                }
            }
        }
        return res;    
    }


    public static void main(String[] args) {
        System.out.println(new Solution().LLCCA(new String[]{"a","b","c"}, new String[]{"a","f","e","b","c"}));
    }
}