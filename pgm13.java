import java.util.Scanner;

public class pgm13 {

    public static void printsum(int n, int m){
        System.out.println("The sum is "+(n+m));
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter two numbers : ");
        int a = sc.nextInt();
        int b = sc.nextInt();

        printsum(a,b);

    }
}
