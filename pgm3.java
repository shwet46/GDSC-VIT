import java.util.Scanner;

public class pgm3 {

    public static void print(String s){

        for(int i= 0; i<s.length(); i++){
            if(i%2 == 0){
                System.out.print(s.charAt(i) + " ");
            }
        }
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String s = sc.next();

        print(s);

    }
}
