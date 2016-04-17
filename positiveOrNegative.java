import java.util.Scanner;
public class positiveOrNegative {
        public static void main(String[] args) {
              Scanner inputScanner = new Scanner(System.in);
		System.out.println("Enter integer: ");
		int Numb = inputScanner.nextInt();
		
		if (Numb > 0) {
		System.out.println("Positive");  
        }
		else if (Numb < 0) {
                System.out.println("Negative");
        }
		else if (Numb == 0){
		System.out.println("Neutral");
	}
}
}
