import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	static boolean isPrimeNumber(int x) {
		for(int i=2; i<Math.sqrt(x)+1;i++) {
			if(x%i == 0) return false;
		}
		return true;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt() - 1;
		ArrayList<Integer>[] dp = new ArrayList[n+1];
		for (int i=0;i<n+1;i++)
			dp[i] = new ArrayList<>();
		dp[0].add(2);
		dp[0].add(3);
		dp[0].add(5);
		dp[0].add(7);
		
		for(int i=1; i<n+1;i++) {
			for (int d=1; d<10;d++) {
				for (int k : dp[i-1]) {
					int tmp = k*10 + d;
					if (isPrimeNumber(tmp)) dp[i].add(tmp);
				}
			}
		}
		dp[n].sort(null);
		for ( int i : dp[n]) System.out.println(i);

	}

}
