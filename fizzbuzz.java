import java.util.Scanner;
public class fizzBuzz{
public static void main(String[] args){
	Scanner inputScanner = new Scanner(System.in);
	System.out.println("Enter integer: ");
	int Numb = inputScanner.nextInt();
	
	if(Numb % 3 == 0 & Numb % 5 == 0){
	System.out.println("FizzBuzz");
}
	else if(Numb % 3 == 0){
System.out.println("Fizz");}

else if(Numb % 5 == 0){
System.out.println("Buzz");}

else{}
}
}
