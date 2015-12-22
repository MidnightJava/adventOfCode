package aoc;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AocDay05 {
	
	private static int niceCount;
	
	private static String[] forbiddenLetters = new String[] {
			"^.*ab.*$", "^.*cd.*$", "^.*pq.*$", "^.*xy.*$"
	};


	public static void main(String[] args) {
		niceStrings();
		niceStrings2();
	}
	
	private static void niceStrings2() {
		try {
			niceStrings2(FileIO.getFileAsList("niceStrings"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static void niceStrings2(List<String> lines) throws IOException {
		niceCount = 0;
		for (String line: lines) {
			if (isNice2(line)) {
				niceCount++;
			}
		}
		System.err.println("Number of Nice Strings2: " + niceCount);
	}

	private static void niceStrings() {
		try {
			niceStrings(FileIO.getFileAsList("niceStrings"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static void niceStrings(List<String> lines) throws IOException {
		niceCount = 0;
		for (String line: lines) {
			if (isNice(line)) {
				niceCount++;
			}
		}
		System.err.println("Number of Nice Strings: " + niceCount);
	}

	private static boolean isNice2(String line) {
		if (hasNonOverlappingPair(line)) {
			if (hasRepeatWithSkip(line)) {
				return true;
			}
		}
		return false;
	}

	private static boolean hasRepeatWithSkip(String line) {
		Map<Character, List<Integer>> map = new HashMap<Character, List<Integer>>();
		char[] chars = new char[line.length()];
		line.getChars(0, line.length(), chars, 0);
		for (int i = 0; i < chars.length; i++) {
			List<Integer> indices = map.get(chars[i]);
			if (indices == null) {
				indices = new ArrayList<Integer>();
				map.put(chars[i], indices);
			}
			indices.add(i);
		}
		for (List<Integer> indices : map.values()) {
			for (int i = 0; i < indices.size(); i++) {
				if (i < indices.size() - 1) {
					for (int j = i +1; j < indices.size(); j++) {
						if ((indices.get(j) - indices.get(i)) == 2) {
							return true;
						}
					}
				}
			}
		}
		return false;
	}

	private static boolean hasNonOverlappingPair(String line) {
		char[] chars = new char[line.length()];
		line.getChars(0, line.length(), chars, 0);
		for (int i = 0; i < chars.length; i++) {
			if (i <= chars.length - 4) {
				for (int j = i+2; j < chars.length -1; j++) {
					if (new String(new char[]{chars[i],chars[i+1]}).equals(
							(new String(new char[]{chars[j],chars[j+1]})))) {
						return true;
					}
				}
			}
		}
		return false;
	}

	private static boolean isNice(String line) {
		if (!hasVowels(line, 3)) {
			return false;
		}
		if (!hasDoubleLetter(line)) {
			return false;
		}
		if (hasForbiddenLetters(line)) {
			return false;
		}
		return true;
	}

	private static boolean hasForbiddenLetters(String line) {
		for (String s : forbiddenLetters) {
			if (Pattern.matches(s, line)) {
				return true;
			}
		}
		return false;

	}

	private static boolean hasDoubleLetter(String line) {
		char[] chars = new char[line.length()];
		line.getChars(0, line.length(), chars, 0);
		for (int i = 0; i < chars.length; i++) {
			if (i < chars.length -1) {
				if (chars[i] == chars[i+1]) {
					return true;
				}
			}
		}
		return false;
	}

	private static boolean hasVowels(String line, int minCount) {
		String regex = "[aeiou]";
		Pattern p = Pattern.compile(regex);
		Matcher m = p.matcher(line);
		int count = 0;
		while (m.find()) {
			count++;
		}
		return count >= minCount;
	}
}
