import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.swt.widgets.Text;
import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Button;
import org.eclipse.wb.swt.SWTResourceManager;
import org.eclipse.swt.events.SelectionAdapter;
import org.eclipse.swt.events.SelectionEvent;

public class Calc {

	protected Shell shell;
	private Text firstNumber;
	private Text secondNumber;

	/**
	 * Launch the application.
	 * @param args
	 */
	public static void main(String[] args) {
		try {
			Calc window = new Calc();
			window.open();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Open the window.
	 */
	public void open() {
		Display display = Display.getDefault();
		createContents();
		shell.open();
		shell.layout();
		while (!shell.isDisposed()) {
			if (!display.readAndDispatch()) {
				display.sleep();
			}
		}
	}

	/**
	 * Create contents of the window.
	 */
	protected void createContents() {
		shell = new Shell();
		shell.setBackground(SWTResourceManager.getColor(SWT.COLOR_LIST_BACKGROUND));
		shell.setSize(450, 300);
		shell.setText("Ed's Java Calculator");
		
		firstNumber = new Text(shell, SWT.BORDER);
		firstNumber.setBounds(130, 39, 200, 19);
		
		secondNumber = new Text(shell, SWT.BORDER);
		secondNumber.setBounds(130, 85, 200, 19);
		
		Label lblNewLabel = new Label(shell, SWT.NONE);
		lblNewLabel.setFont(SWTResourceManager.getFont("Lucida Grande", 11, SWT.NORMAL));
		lblNewLabel.setBounds(187, 19, 89, 14);
		lblNewLabel.setText("First Number");
		
		Label lblSecondNumber = new Label(shell, SWT.NONE);
		lblSecondNumber.setFont(SWTResourceManager.getFont("Lucida Grande", 11, SWT.NORMAL));
		lblSecondNumber.setBounds(183, 65, 106, 14);
		lblSecondNumber.setText("Second Number");
		
		final Label answerLabel = new Label(shell, SWT.NONE);
		answerLabel.setForeground(SWTResourceManager.getColor(0, 0, 0));
		answerLabel.setBackground(SWTResourceManager.getColor(255, 255, 255));
		answerLabel.setFont(SWTResourceManager.getFont("Lucida Grande", 15, SWT.NORMAL));
		answerLabel.setBounds(164, 185, 200, 28);
		answerLabel.setText("Answer = ");
		
		Button subtractButton = new Button(shell, SWT.NONE);
		subtractButton.addSelectionListener(new SelectionAdapter() {
			@Override
			public void widgetSelected(SelectionEvent e) {
				int number1, number2;
				try{
					number1 = Integer.parseInt(firstNumber.getText());
				
				}
				catch(Exception exec){
					MessageDialog.openError(shell, "Error", "Non integer entered in first number field"); 
					return; 
				}
				try{
					number2 = Integer.parseInt(secondNumber.getText());
				
				}
				catch(Exception exec){
					MessageDialog.openError(shell, "Error", "Non integer entered in second number field"); 
					return; 
				}
				int answer = number1 - number2;
				answerLabel.setText("Answer = " + answer); 
			}
		
		});
		subtractButton.setToolTipText("Subtract");
		subtractButton.setBounds(171, 114, 46, 28);
		subtractButton.setText("-");
		

		
		
		Button plusButton = new Button(shell, SWT.NONE);
		plusButton.addSelectionListener(new SelectionAdapter() {
			@Override
			public void widgetSelected(SelectionEvent e) { 
				int number1, number2;
				try{
					number1 = Integer.parseInt(firstNumber.getText());
				
				}
				catch(Exception exec){
					MessageDialog.openError(shell, "Error", "Non integer entered in first number field"); 
					return; 
				}
				try{
					number2 = Integer.parseInt(secondNumber.getText());
				
				}
				catch(Exception exec){
					MessageDialog.openError(shell, "Error", "Non integer entered in second number field"); 
					return; 
				}
				int answer = number1 + number2;
				answerLabel.setText("Answer = " + answer); 
			}
		});
		
		plusButton.setToolTipText("Add");
		plusButton.setBounds(130, 114, 46, 28);
		plusButton.setText("+");
		
		Button xButton = new Button(shell, SWT.NONE);
		xButton.addSelectionListener(new SelectionAdapter() {
			@Override
			public void widgetSelected(SelectionEvent e) { 
				int number1, number2;
				try{
					number1 = Integer.parseInt(firstNumber.getText());
				
				}
				catch(Exception exec){
					MessageDialog.openError(shell, "Error", "Non integer entered in first number field"); 
					return; 
				}
				try{
					number2 = Integer.parseInt(secondNumber.getText());
				
				}
				catch(Exception exec){
					MessageDialog.openError(shell, "Error", "Non integer entered in second number field"); 
					return; 
				}
				int answer = number1 * number2;
				answerLabel.setText("Answer = " + answer); 
			}
		});
		xButton.setToolTipText("Multiply");
		xButton.setBounds(243, 114, 46, 28);
		xButton.setText("x");
		
		
		Button divideButton = new Button(shell, SWT.NONE);
		divideButton.addSelectionListener(new SelectionAdapter() {
			@Override
			public void widgetSelected(SelectionEvent e) { 
				int number1, number2;
				try{
					number1 = Integer.parseInt(firstNumber.getText());
				
				}
				catch(Exception exec){
					MessageDialog.openError(shell, "Error", "Non integer entered in first number field"); 
					return; 
				}
				try{
					number2 = Integer.parseInt(secondNumber.getText());
				
				}
				catch(Exception exec){
					MessageDialog.openError(shell, "Error", "Non integer entered in second number field"); 
					return; 
				}
				int answer = number1 / number2;
				answerLabel.setText("Answer = " + answer); 
			}
		});
		divideButton.setToolTipText("Divide");
		divideButton.setBounds(284, 114, 46, 28);
		divideButton.setText("/");
		

	}
}
