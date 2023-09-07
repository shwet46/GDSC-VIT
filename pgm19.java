import java.util.Random;
import java.util.Scanner;

public class pgm19 {
    public static void main(String[] args) {

        int answer,guess;

        final int MAX = 100;

        Scanner sc = new Scanner(System.in);

        Random rand = new Random();

        boolean correct = false;

        answer = rand.nextInt(MAX)+1;

        while(!correct){

            System.out.print("Guess a number between 1 to 100 : ");

            guess = sc.nextInt();

            if(guess>answer){
                System.out.println("Too high, try again !");
            }
            else if(guess<answer){
                System.out.println("Too low, try again !");
            }
            else{
                System.out.println("Yes, you guessed the number !!");
                correct = true;
            }

        }

        System.exit(0);


    }
}
