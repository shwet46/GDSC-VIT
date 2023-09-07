public class pgm15 {

    public static void fib(int n){
        int t1 = 0;
        int t2 = 1;
        int nt = 0;
        for(int i=0; i<n; i++){
            System.out.print(t1+" ");
            nt = t1+t2;
            t1 = t2;
            t2 = nt;
        }
    }
    public static void main(String[] args) {

        fib(10);

    }
}
