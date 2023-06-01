import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		String[] A = s.split("-", 2);
		int sum = 0;
		for(String a : A[0].split("\\+")) sum += Integer.parseInt(a);
		if(A.length==2) {
			for(String a : A[1].split("-|\\+")) sum-= Integer.parseInt(a);
		}
		System.out.println(sum);	
	}
}
