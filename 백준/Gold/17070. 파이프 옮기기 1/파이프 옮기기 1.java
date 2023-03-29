import java.util.Scanner;

public class Main {
    static int[] dr = {0, -1, -1};
    static int[] dc = {-1, 0, -1};
    static int[][] dt = {{0, 2}, {1, 2}, {0, 1, 2}};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] graph = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                graph[i][j] = sc.nextInt();
            }
        }
    
        int[][][] dp = new int[N][N][3];
        dp[0][1] = new int[]{1, 0, 0};
    
        for (int r = 0; r < N; r++) {
            for (int c = 2; c < N; c++) {
                if (graph[r][c] == 1) {
                    continue;
                }
                for (int d = 0; d < 3; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                        if (d == 2) {
                            if (graph[r - 1][c] == 1 || graph[r][c - 1] == 1) {
                                continue;
                            }
                            dp[r][c][d] = dp[nr][nc][dt[d][0]] + dp[nr][nc][dt[d][1]] + dp[nr][nc][dt[d][2]];
                        } else {
                            dp[r][c][d] = dp[nr][nc][dt[d][0]] + dp[nr][nc][dt[d][1]];
                        }
                    }
                }
            }
        }
    
        int answer = dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2];
        System.out.println(answer);
    }
}
