import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {

    static ArrayList<Integer> map[] = new ArrayList[10];
    static int paper[] = {0,5,5,5,5,5};
    static int res = 987654321;
    static int cnt = 0;

    static void run(int y, int x){
        if(x == 10){
            run(y+1,0);
            return;
        }
        if(y == 10){
            res = Math.min(res, cnt);
            return;
        }
        if(map[y].get(x) == 0){
            run(y, x+1);
            return;
        }
        for (int leng = 5;leng > 0;leng--) {
            if (paper[leng] == 0 || y + leng > 10 || x + leng > 10) {
                continue;
            }
            boolean flag = false;

            for (int j = 0;j < leng;j++) {
                for (int k = 0;k < leng;k++) {
                    if (map[y + j].get(x + k) == 0) {
                        flag = true;
                        break;
                    }
                }
                if (flag) {
                    break;
                }
            }
            if (flag) {
                continue;
            }

            for (int j = 0;j < leng;j++) {
                for (int k = 0;k < leng;k++) {
                    map[y + j].set(x + k, 0);
                }
            }
            paper[leng]--;
            cnt++;

            run(y, x + leng);

            for (int j = 0;j < leng;j++) {
                for (int k = 0;k < leng;k++) {
                    map[y + j].set(x + k, 1);
                }
            }
            paper[leng]++;
            cnt--;
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        for(int i=0;i<10;i++){
            map[i] = new ArrayList<Integer>();
        }

        for(int i=0;i<10;i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0;j<10;j++){
                int a = Integer.parseInt(st.nextToken());
                map[i].add(a);
            }
        }

        run(0,0);

        if(res == 987654321){
            System.out.println(-1);
        }else{
            System.out.println(res);
        }
    }
}
