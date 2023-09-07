import java.util.Scanner;

public class pgm12 {

    public static void oddeven(int n){
        if(n%2 == 0){
            System.out.println(n+" is even.");
        }
        else{
            System.out.println(n+" is odd.");
        }
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        oddeven(n);

    }
}
