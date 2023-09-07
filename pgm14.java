public class pgm14 {

    public static void factorial(int n){
        if(n>=0){
            int f = 1;
            for(int i=1; i<=n; i++){
                f *= i;
            }
            System.out.println("the factorial of "+n+" is "+f);
        } else if (n<0) {
            System.out.println("factorial does not exist for negative numbers");
        } else{
            System.out.println("Invalid input");
        }
    }
    public static void main(String[] args) {

       factorial(5);

    }
}
