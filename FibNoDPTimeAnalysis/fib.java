public class Fib {
	static int fib(int n) {
		if (n == 0 || n == 1)
			return n;
		return fib(n - 1) + fib(n - 2);
	}
	public static void main(String[] args) {
		long startTime = System.currentTimeMillis();
		int res = fib(35);
		long stopTime = System.currentTimeMillis();
	    long elapsedTime = stopTime - startTime;
	    System.out.println(elapsedTime); // ms
	}
}

