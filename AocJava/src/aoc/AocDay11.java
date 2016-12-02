package aoc;

import java.util.regex.Pattern;

public class AocDay11 {

	public static void main(String[] args) {
		String password = "hepxcrrq";
		while (!isValid(password = increment(password)));
		System.out.println("password1: " + password);
		while (!isValid(password = increment(password)));
		System.out.println("password2: " + password);
	}

	private static boolean isValid(String password) {
		return  Pattern.matches(".*(.)\\1.*(.)\\2.*", password)
				&& Pattern.matches(".*(abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz).*", password)
				&& !Pattern.matches("[ilo]", password);
	}

	private static String increment(String password) {
		return  Long.toString(Long.parseLong(password, 36) +1, 36).replace('0', 'a');
	}
}
	