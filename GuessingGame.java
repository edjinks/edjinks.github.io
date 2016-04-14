import java.util.Random;
import java.util.Scanner;
public class GuessingGame {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Random rand = new Random();
		int numberToGuess = rand.nextInt(1000);
		
		int numberOfTries = 0;
		Scanner input = new Scanner(System.in);
		int guess;
		boolean win = false;
		
		while (win == false) {		
		System.out.println("Guess a number between 1 - 1000: ");
		guess = input.nextInt();
		numberOfTries++;
		if (guess == numberToGuess) {
			 win = true;
		}
		else if (guess < numberToGuess) {
			System.out.println("Too Low");
		}
		else if (guess > numberToGuess) {
			System.out.println("Too High");
	}
		}
		
System.out.println("Winner");
System.out.println("The number was " +numberToGuess);
System.out.println("It took you " +numberOfTries+ " tries");
}
}
