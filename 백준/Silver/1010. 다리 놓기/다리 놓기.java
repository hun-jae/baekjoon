import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        for (int i = 0; i < t; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int[] dp = new int[b+1];
            dp[a] = 1;
            for (int n = a+1; n <= b; n++) {
                dp[n] = n*dp[n-1]/(n-a);
            }
            System.out.println(dp[b]);
        }
    }
}
