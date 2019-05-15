package ui;

import java.util.Map;
import java.util.Scanner;

import exception.EmptyCommandException;

public class Cli {
	
	public Cli() {
		run();
	}
	
	public void run() {
		//Setup input environment
		Scanner sc = new Scanner(System.in);
		while(true) {
			//Setup input line and get command string
			System.out.print(">>>");
			String cmd_string = sc.nextLine();
			//Process Commands
			try {
				if(!proccessCommand(cmd_string)) {
					break;
				}
			//Error Handling
			} catch (EmptyCommandException e) {
				System.out.println("You have entered an empty command. Try again:");
			}
		}
	}

	private boolean proccessCommand(String cmd_string) throws EmptyCommandException {
		// TODO Auto-generated method stub
		System.out.println(cmd_string);
		//Check string parts and take string apart
		Command cmd = cmd_components(cmd_string);
		
		if (cmd_string.equalsIgnoreCase("Exit")) {
			//Exit Cli loop with false
			return false;
		}
		
		//Continue the Cli loop with True
		return true;
	}

	private Command cmd_components(String cmd_string) throws EmptyCommandException {
		// TODO Auto-generated method stub
		//Check empty String
		if (cmd_string == null || cmd_string.isEmpty()) {
			throw new EmptyCommandException();
		}
		
		//Split string with white space char.
		String[] cmd = cmd_string.split(" ");
		
		//Check if command exists against command array.
		
		
		//Check argument number and validity against regular expressions.
		
		//Return properly formatted Command object containing command and arguments.
		
		return null;
	}

}
