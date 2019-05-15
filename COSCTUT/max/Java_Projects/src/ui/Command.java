package ui;

import java.util.Map;

public class Command {
	
	private String command;
	private Map<String, String> arguments;
	
	public Command(String command, Map<String, String> arguments) {
		this.command = command;
		this.arguments = arguments;
	}
	
	public String getCommand() {
		return this.command;
	}
	
	public Map<String, String> getArguments() {
		return this.arguments;
	}

}
