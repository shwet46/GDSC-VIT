public class pgm1 {

    public static int operation(int a, int b){
        int prod = a*b;
        int sum = a+b;

        if(prod<=1000){
            return prod;
        }
        else{
            return sum;
        }
    }
    public static void main(String[] args) {

        System.out.println(operation(45,56));

    }
}
