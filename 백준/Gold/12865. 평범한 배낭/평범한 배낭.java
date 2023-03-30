import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		int[][] things = new int[n][2];
		int[][] napsack = new int[n+1][k+1];
		for (int i=0;i<n;i++) {
			st = new StringTokenizer(br.readLine());
			things[i][0] = Integer.parseInt(st.nextToken());
			things[i][1] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(things, (o1, o2) -> Integer.compare(o1[0], o2[0]) );

		for (int i=1;i<n+1;i++) {
			int weight = things[i-1][0];
			int value = things[i-1][1];
			for (int j=0;j<k+1;j++) {
				if (weight > j) {
					napsack[i][j] = napsack[i-1][j];
				}
				else {
					napsack[i][j] = Math.max(napsack[i-1][j], napsack[i-1][j-weight] + value);
				}
			}
		}
		System.out.println(napsack[n][k]);
	}
}
