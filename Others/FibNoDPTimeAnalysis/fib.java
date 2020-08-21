public class Fib {
	static int fib(int n) {
		if (n == 0 || n == 1)
			return n;
		return fib(n - 1) + fib(n - 2);
	}
	public static void main(String[] args) {
		int N = Integer.parseInt(args[0]);
		long startTime, endTime, elapsedTime;
		startTime = System.nanoTime();
		fib(N);
		endTime = System.nanoTime()
	    elapsedTime = (endTime - startTime);
	    System.out.println("java " + elapsedTime); // ms
	}
}

