import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int[][] graph;
	static boolean[][][] visited;

	static int[] dx = { 0, 0, 1, -1 };
	static int[] dy = { 1, -1, 0, 0 };
	static int[] horse_dx = { -2, -2, -1, -1, 1, 1, 2, 2 };
	static int[] horse_dy = { -1, 1, -2, 2, -2, 2, -1, 1 };
	static int K, W, H;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		K = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		W = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());

		graph = new int[H][W];
		visited = new boolean[H][W][K + 1];
		for (int i = 0; i < H; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < W; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				for (int k = 0; k < K; k++) {
					visited[i][j][k] = false;
				}
			}
		}

		
		if (W==1 && H==1)
		    System.out.println(0);
		else
		    System.out.println(bfs());
	}

	public static int bfs() {
		Queue<int[]> que = new ArrayDeque<int[]>();
		que.add((new int[] { 0, 0, 0 }));
		int size;
		int cnt = 1;
		while (!que.isEmpty()) {
			size = que.size();
			for (int i = 0; i < size; i++) {
				int[] xyk = que.poll();
				int x = xyk[0];
				int y = xyk[1];
				int k = xyk[2];

				for (int d = 0; d < 4; d++) {
					int nx = x + dx[d];
					int ny = y + dy[d];
					if (0 <= nx && nx < H && 0 <= ny && ny < W && !visited[nx][ny][k] && graph[nx][ny] == 0) {
						if (nx == H - 1 && ny == W - 1)
							return cnt;
						visited[nx][ny][k] = true;
						que.add(new int[] { nx, ny, k });
					}
				}
				if (k < K) {
					for (int d = 0; d < 8; d++) {
						int nx = x + horse_dx[d];
						int ny = y + horse_dy[d];
						if (0 <= nx && nx < H && 0 <= ny && ny < W && !visited[nx][ny][k + 1] && graph[nx][ny] == 0) {
							if (nx == H - 1 && ny == W - 1)
								return cnt;
							visited[nx][ny][k + 1] = true;
							que.add(new int[] { nx, ny, k + 1 });
						}
					}
				}
			}
			cnt++;
		}
		return -1;
	}

}
