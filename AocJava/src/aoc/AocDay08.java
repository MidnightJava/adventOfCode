package aoc;

import java.io.IOException;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AocDay08 {
	
	private static int deltaChars = 0;

	public static void main(String[] args) {
		
		//Java 8 implementation from reddit user
		List<String> input = null;
		input  = FileIO.getFileAsList("input.txt");

		int literals = FileIO.getFileAsList("input.txt").stream()
				.mapToInt(x -> x.length())
				.sum();

		int memory = input.stream()
				.map(x -> x.replace("\\\\", "S"))
				.map(x -> x.replace("\\\"", "Q"))
				.map(x -> x.replaceAll("\"", ""))
				.map(x -> x.replaceAll("\\\\x[0-9a-f]{2}", "X"))
				.mapToInt(x -> x.length())
				.sum();

		System.out.println(literals - memory);

		// part 2

		int embiggen = input.stream()
				.map(x -> x.replaceAll("\\\\x[0-9a-f]{2}", "XXXXX"))
				.map(x -> x.replace("\\\"", "QQQQ"))
				.map(x -> x.replace("\\\\", "SSSS"))
				.mapToInt(x -> x.length() + 4)
				.sum();

		System.out.println(embiggen - literals);
		
		escapes();

	}
	
	//clunky implementation. See python implementation for parts 1 and 2
	private static void escapes() {
		try {
			escapes(FileIO.getFileAsList("escapes"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static void escapes(List<String> lines) throws IOException {
		for (String line: lines) {
			calcDiff(line);
		}
		System.err.println("Code - mem difference: " + deltaChars);
	}

	private static void calcDiff(String line) {
		line = line.replaceAll("\\s", "").replaceFirst("^\"", "").replaceFirst("\"$", "");
		String regex = "\\\\\\\"";
		Pattern p = Pattern.compile(regex);
		Matcher m = p.matcher(line);
		int quotes = 2;
		while (m.find()) {
			quotes++;
		}

		regex = "\\\\[xX][0-9a-fA-F]{2}";
		p = Pattern.compile(regex);
		m = p.matcher(line);
		int escapeChars = 0;
		while (m.find()) {
			escapeChars+= 3;
		}

		regex = "\\\\\\\\";
		p = Pattern.compile(regex);
		m = p.matcher(line);
		int slashes = 0;
		while (m.find()) {
			slashes++;
		}

		int codeChars = line.length();
		int memChars = line.length() - quotes - escapeChars - slashes;
		int diff = codeChars - memChars;
		deltaChars+= diff;
	}
}
