package aoc;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AocDay11Original {

	public static void main(String[] args) {
		String password = "hepxcrrq";
		while (!isValid(password = increment(password)));
		System.out.println("password1: " + password);
		while (!isValid(password = increment(password)));
		System.out.println("password2: " + password);
	}

	private static boolean isValid(String password) {
		Map<Character, Integer > foundCharPairs = new HashMap<Character, Integer>();
		boolean foundPairs = false;
		for (int i = 0; i <= password.length()-2; i++) {
			char c = password.charAt(i);
			if (password.charAt(i+1) == c) {
				foundCharPairs.put(c, i);
				for (Entry<Character, Integer> entry : foundCharPairs.entrySet()) {
					if (entry.getKey() != c && Math.abs(entry.getValue() - i) > 1) {
						foundPairs = true;
						break;
					}
				}
			}
		}
		if (foundPairs) {
			for (int i = 0; i <= password.length()-3; i++) {
				char c = password.charAt(i);
				if (password.charAt(i+1) == (c +1) && password.charAt(i+2) == (c +2)) {
					return true;
				}
			}
		}
		return false;
	}

	private static String increment(String password) {
		String regex = "(z+)$";
		Matcher m = Pattern.compile(regex).matcher(password);
		if (m.find()) {
			if (password.equals("zzzzzzzz")) {
				return "aaaaaaaa";
			}
			password = password.substring(0, password.length() - m.group(1).length());
			String repl = "";
			for (int i = 1; i <= m.group(1).length(); i++) {
				repl+= "a";
			}
			password+= repl;
			char c = password.charAt(password.length() - (m.group(1).length() + 1));
			if (c == 'h' || c == 'n' || c=='k') {
				c+= 2;
			} else {
				c++;
			}
			return password.substring(0,  password.length() - (m.group(1).length() + 1)) + c
					+ password.substring( password.length() - m.group(1).length(), password.length());
		} else {
			char c = password.charAt(password.length() -1);
			if (c == 'h' || c == 'n' || c=='k') {
				c+= 2;
			} else {
				c++;
			}
			return password.substring(0, password.length() -1) + c;
		}
	}
}