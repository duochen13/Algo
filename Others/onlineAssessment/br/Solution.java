import java.util.ArrayList;
import java.util.Set;


class ChangeCalculator {
  
  public static final double[] coins = new double[]{1, 2, 5};
  public double amount;

  ChangeCalculator(double amount) { this.amount = amount; }


  public double[] coinChange() {
    int N = (int)this.amount;
    Map<Double> memo = new HashMap<Double>();
    memo.put(0, 0);

    for (int x = 0; x < N + 1; ++i) {
      for (double coin : coins) {
        if (x >= coin) {
          if (!memo.containsKey(x)) {
            memo.put(x, Math.min(memo.get(x), memo.get(x - coin) + 1));
          }
        }
      }
    }

    return new double[]{1.0};
  }
}




class Solution {

    public static void main(String[] args) {
        
      Solution s = new Solution();
      ChangeCalculator cc = new ChangeCalculator(11.0);
      cc.coinChange();
    }

}