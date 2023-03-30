
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	static int N;
	static int graph[][];
	static boolean visited[][];
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int cnt = 0;
		while(true) {
			cnt++;
			N = sc.nextInt();
			if(N==0) break;
			graph = new int[N][N];
			visited = new boolean[N][N];
			for(int i=0; i<N; i++) {
				for (int j = 0; j < N; j++) {
					graph[i][j] = sc.nextInt();
					visited[i][j] = false;
				}
			}
			visited[0][0] = true;
			System.out.printf("Problem %d: %d\n", cnt, dij());
		}
		
		
	}
	public static int dij() {
		PriorityQueue<Node> q = new PriorityQueue<>();
		q.add(new Node(0, 0, graph[0][0]));
		while (!q.isEmpty()) {
			Node curNode = q.poll();
			for(int d=0; d<4; d++) {
				int nx = curNode.x + dx[d];
				int ny = curNode.y + dy[d];
				if(nx < 0 || nx >= N || ny < 0 || ny >= N) continue;
				if(visited[nx][ny]) continue;
				visited[nx][ny] = true;
				graph[nx][ny] += curNode.dist;
				if (nx == N-1 && ny == N-1) {					
					return graph[nx][ny];
				}
				q.add(new Node(nx, ny, graph[nx][ny]));
			}
		}
		return 0;
	}

	public static class Node implements Comparable<Node>{
		int x;
		int y;
		int dist;
		public Node(int x, int y, int dist) {
			super();
			this.x = x;
			this.y = y;
			this.dist = dist;
		}
		@Override
		public int compareTo(Node o) {
			return this.dist - o.dist;
		}
		
	}
}

