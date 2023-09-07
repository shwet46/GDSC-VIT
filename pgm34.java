import java.util.Scanner;

public class pgm34 {

    public static void main(String[] args) {

       Scanner sc = new Scanner(System.in);

       int n = sc.nextInt();
       int a[] = new int[n];

        System.out.print("Enter array Elements : ");
        for(int i=0; i<n; i++){
            a[i] = sc.nextInt();
        }

        boolean swap = false;

        for(int i=0; i<a.length-1; i++){
            for(int j=0; j<a.length-i-1; j++){
                if(a[j] > a[j+1]){
                    int temp = a[j];
                    a[j] = a[j+1];
                    a[j+1] = temp;
                    swap = true;
                }
            }
            if(!swap){
                break;
            }
        }

        System.out.print("Sorted array : ");

        for(int i=0; i<a.length; i++){
            System.out.print(a[i]+" ");
        }

    }
}
