package aoc;

import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AocDay10 {
	//part1 252594
	//part2 3579328

	public static void main(String[] args) {
		String input = "1113222113";
		System.err.println("Part1 Output length: " + lookAndSay(input, 40).length());
		System.err.println("Part2 Output length: " + lookAndSay(input, 50).length());

		System.err.println("Part1 Output length: " + lookAndSay2(input, 40).length());
		System.err.println("Part2 Output length: " + lookAndSay2(input, 50).length());
	}

	private static String lookAndSay(String input, int numIter) {
		StringBuilder sb = null;
		for (int i = 1; i <= numIter; i++) {
			sb = new StringBuilder();
			int j = 1, count = 1, c = 0;
			char lastChar = input.charAt(0);
			while (j < input.length()-1) {
				while ((c = input.charAt(j++)) == lastChar) {
					count++;
				}
				sb.append(String.valueOf(count) + lastChar);
				count = 1;
				lastChar = input.charAt(j-1);
			}
			sb.append(String.valueOf(count) + lastChar);
			input = sb.toString();
		}
		return sb.toString();
	}

	//second approach inspired by reddit user merdada
	private static String lookAndSay2(String input, int numIter) {
		String[] a = new String[numIter];
		a[0] = input;
		return Arrays.stream(a).reduce(input,  (s, x) -> lookAndSay(s));
	}

	private static String lookAndSay(String s) {
		Matcher m  = Pattern.compile("(\\d)\\1*").matcher(s);
		StringBuilder sb = new StringBuilder();
		while (m.find()) {
			sb.append(String.valueOf(m.group().length()) + m.group().charAt(0));
		}
		return sb.toString();
	}
}
