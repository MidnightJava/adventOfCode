package aoc;

import java.util.HashMap;
import java.util.IntSummaryStatistics;
import java.util.List;
import java.util.Map;

import com.google.common.collect.Collections2;

public class AocDay09 {

	private static Map<String, Map<String, Integer>> routes = new HashMap<String, Map<String, Integer>>();

	public static void main(String[] args) {
		FileIO.getFileAsStream("input-9.txt").forEach(e -> processEntry(e));
		
		IntSummaryStatistics stats = Collections2.permutations(routes.keySet()).stream()
		.mapToInt(l -> computeDistance(l))
		.summaryStatistics();

		System.err.println("min value is " + stats.getMin());
		System.err.println("max value is " + stats.getMax());

	}

	private static int computeDistance(List<String> l) {
		int distance = 0;
		for (int i = 0; i < (l.size() - 1); i++) {
			distance += findDistance(l.get(i), l.get(i+1));
		}
		return distance;
	}

	private static int findDistance(String s1, String s2) {
		return routes.get(s1).get(s2);
	}

	private static void processEntry(String s) {
		String[] parts = s.split("\\s");
		if (parts.length == 5) {
			String from = parts[0], to = parts[2], dist = parts[4];
			Map<String, Integer> entry = routes.get(from);
			if (entry == null) {
				entry = new HashMap<String, Integer>();
				routes.put(from, entry);
			}
			entry.put(to, new Integer(dist));

			entry = routes.get(to);
			if (entry == null) {
				entry = new HashMap<String, Integer>();
				routes.put(to, entry);
			}
			entry.put(from, new Integer(dist));
		}
	}
}

