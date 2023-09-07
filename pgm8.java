public class pgm8 {

    public static void checkPal(int n){
        int d = 0;
        int r = 0;
        int temp = n;

        while(n>0){
            d = n%10;
            r = r*10+d;
            n /=10;
        }

        if(temp == r){
            System.out.println(temp +" is palindrome");
        }
        else{
            System.out.println(temp + " is not palindrome.");
        }
    }
    public static void main(String[] args) {

        checkPal(545);
        checkPal(1234);

    }
}
