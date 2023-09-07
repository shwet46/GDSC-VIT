public class pgm16 {

    public static void prime(int n){
        int c = 0;
        for(int i=1; i<=n; i++){
            if(n%i == 0){
                c++;
            }
        }

        if(c == 2){
            System.out.println(n+" is a prime number");
        }
        else{
            System.out.println(n+" is not a prime number");
        }
    }

    public static void main(String[] args) {

        prime(7);
        prime(15);

    }
}
