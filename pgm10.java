public class pgm10 {

    public static void printNum(int n){
        int d = 0;
        int r = 0;
        while(n>0){
            d = n%10;
            n /= 10;
            System.out.print(d+" ");
        }
    }
    public static void main(String[] args) {

        printNum(7536);

    }
}
