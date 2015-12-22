package aoc;

import java.io.IOException;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class AocDay02 {
	
	private static class Measurements {

		public int width;

		public int length;

		public int height;
	}

	public static void main(String[] args) {
		try {
			calculatePaperArea(FileIO.getFileAsList("wrappinginput"));
			calculateRibbonLength(FileIO.getFileAsList("wrappinginput"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	private static void calculatePaperArea(List<String> lines) throws IOException {
		int area = 0;
		for (String line: lines) {
			Measurements m = getMeasurements(line);
			area+= 2*m.length *m.width;
			area+= 2*m.width* m.height;
			area+= 2*m.height* m.length;
			area+= minDimension(m);
		}
		System.err.println("TOTAL AREA: " + area);
	}

	private static void calculateRibbonLength(List<String> lines) throws IOException {
		int length = 0;
		for (String line : lines) {
			Measurements m = getMeasurements(line);
			length += Math.min(Math.min(2 * (m.width + m.height), 2 * (m.width + m.length)), 2 * (m.height + m.length));
			length+= m.width * m.height * m.length;
		}
		System.err.println("TOTAL LENGTH: " + length);
	}
	
	private static int minDimension(Measurements m) {
		return Math.min(Math.min(m.length * m.width, m.length * m.height), m.width * m.height);
	}

	private static Measurements getMeasurements(String line) {
		Measurements m = new Measurements();
		String regex = "^(\\d+)x(\\d+)x(\\d+)$";
		Pattern p = Pattern.compile(regex);
		Matcher matcher = p.matcher(line);
		if (matcher.matches()) {
			m.length = Integer.parseInt(matcher.group(1));
			m.width = Integer.parseInt(matcher.group(2));
			m.height = Integer.parseInt(matcher.group(3));
		} else {
			throw new IllegalArgumentException("Could not match diemnsion string");
		}
		return m;
	}
}
