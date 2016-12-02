package aoc;

import java.nio.charset.Charset;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import com.google.gson.Gson;

public class AocDay12 {

	public static void main(String[] args) {
		String json = FileIO.getFileAsString("json.txt", Charset.defaultCharset());
		Gson gson = new Gson();
		Map<String, Object> contents = (Map<String, Object>) gson.fromJson(json, Object.class);
		System.err.println("Sum of numbers: " + sumNumbers(contents, false));
		System.err.println("Sum of numbers: " + sumNumbers(contents, true));
		System.err.println("Sum of numbers: " + sumNumbers2(json, true));
	}

	private static Integer sumNumbers(Object obj, boolean ignoreRed) {
		int sum = 0;
		if (obj instanceof Map) {
			for (Entry<String, Object> entry : ((Map<String, Object>) obj).entrySet()) {
				if (ignoreRed && "red".equals(entry.getValue())) {
					return 0;
				}
				sum += sumNumbers(entry.getValue(), ignoreRed);
			}
			return sum;
		} else if (obj instanceof List) {
			for ( Object item : (List) obj) {
				sum += sumNumbers(item, ignoreRed);
			}
			return sum;
		} else if (obj instanceof Number) {
			return ((Double) obj).intValue();
		}
		return 0;
	}
	
	//part 1 with regex. Part 2 not so easy
	private static Integer sumNumbers2(String json, boolean ignoreRed) {
		int sum = 0;
		Matcher m= Pattern.compile("(-*\\d++)").matcher(json);
		while (m.find()) {
			sum += Integer.parseInt(m.group(1));
		}
		
		return sum;
	}
}
