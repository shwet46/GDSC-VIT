import java.util.Scanner;

public class pgm23 {
    

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter size of matrix : ");
        int n = sc.nextInt();
        int m = sc.nextInt();

        int a1[][] = new int[n][m];
        int a2[][] = new int[n][m];
        int a3[][] = new int[n][m];



        System.out.println("enter elements of matrix 1 : ");
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                a1[i][j] = sc.nextInt();
            }
        }

        System.out.println("enter elements of Matrix 2 : ");
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                a2[i][j] = sc.nextInt();
            }
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                a3[i][j] = 0;
                for(int k=0; k<n; k++){
                    a3[i][j] += a1[i][k] * a2[k][j];
                    System.out.print(a3[i][j]+" ");
                }
                System.out.println();
            }
        }


    }
}
