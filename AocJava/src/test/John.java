package test;

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.util.Arrays;
import java.util.IntSummaryStatistics;
import java.util.Map;
import java.util.Map.Entry;
import java.util.TreeMap;

/**
 * 
 * @author Mark Leone
 * 
 * Demonstrate Stream API by analyzing the text of John 1:1-18
 *
 */
public class John {
	
	static Map<String, Integer> dict = new TreeMap<String, Integer>();
	private static IntSummaryStatistics stats;

	public static void main(String[] args) {
		String[] words = getFileAsString("john.txt").toLowerCase().replaceAll("\\W", " ").split("\\s");
		Arrays.asList(words).stream()
				.filter(w -> w.length() > 0)
				.map(word -> {dict.put(word, word.length()); return word;})
				.mapToInt(word -> word.length())
				.summaryStatistics();
		printStats();
	}

	private static void printStats() {
		System.out.println("Number of words: " + stats.getCount());
		System.out.println("Shortest word: " + stats.getMin());
		System.out.println("Longest word: " + stats.getMax());
		System.out.println("Number of non-white space characters: " + stats.getSum() + "\n");
		for ( Entry<String, Integer> entry : dict.entrySet()) {
			System.out.println(entry.getKey() + ":" + entry.getValue());
		}

	}
	
	public static String getFileAsString(String file) {
		try {
			byte[] encoded = Files.readAllBytes(FileSystems.getDefault().getPath(".", file));
			return new String(encoded, Charset.defaultCharset());
		} catch (IOException e) {
			e.printStackTrace();
			return "";
		}
		
	}

}
