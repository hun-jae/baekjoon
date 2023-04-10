
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int R = scanner.nextInt();
        int C = scanner.nextInt();
        int N = scanner.nextInt();
        char[][] graph = new char[R][C];
        
        for (int i = 0; i < R; i++) {
            String row = scanner.next();
            for (int j = 0; j < C; j++) {
                graph[i][j] = row.charAt(j);
            }
        }
        
        int[] di = {1, -1, 0, 0};
        int[] dj = {0, 0, 1, -1};
        
        if (N % 2 == 0) {
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    System.out.print("O");
                }
                System.out.println();
            }
        } else {
            if (N == 1) {
                print(graph);
            } else {
                change(graph, di, dj, R, C);
                if ((N - 3) % 4 == 0) {
                    print(graph);
                } else {
                    change(graph, di, dj, R, C);
                    print(graph);
                }
            }
        }
    }
    
    public static void change(char[][] graph, int[] di, int[] dj, int R, int C) {
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (graph[i][j] == 'O') {
                    for (int d = 0; d < 4; d++) {
                        int ni = i + di[d];
                        int nj = j + dj[d];
                        if (0 <= ni && ni < R && 0 <= nj && nj < C && graph[ni][nj] != 'O') {
                            graph[ni][nj] = 'X';
                        }
                    }
                }
            }
        }
        
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (graph[i][j] != '.') {
                    graph[i][j] = '.';
                } else {
                    graph[i][j] = 'O';
                }
            }
        }
    }
    
    public static void print(char[][] graph) {
        for (char[] row : graph) {
            for (char c : row) {
                System.out.print(c);
            }
            System.out.println();
        }
    }
}
