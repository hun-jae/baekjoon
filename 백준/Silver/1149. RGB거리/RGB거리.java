import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int[][] graph = new int[n][3];
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int t=0; t<3; t++) {
				graph[i][t] = Integer.parseInt(st.nextToken());
				if(i!=0) graph[i][t] += Math.min(graph[i-1][(t+1)%3], graph[i-1][(t+2)%3]);
			}
		}
		int result = 10000000;
		for(int t=0; t<3; t++) {
			if (graph[n-1][t] < result) result = graph[n-1][t];
		}
		System.out.println(result);
	}
}