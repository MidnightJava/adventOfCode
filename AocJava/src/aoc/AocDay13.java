package aoc;

import java.util.HashMap;
import java.util.IntSummaryStatistics;
import java.util.List;
import java.util.Map;

import com.google.common.collect.Collections2;

public class AocDay13 {

	private static Map<String, Map<String, Integer>> seatMap = new HashMap<String, Map<String, Integer>>();

	public static void main(String[] args) {
		FileIO.getFileAsStream("seating.txt").forEach(e -> processEntry(e, false));

		IntSummaryStatistics stats = Collections2.permutations(seatMap.keySet()).stream()
				.mapToInt(l -> computeHappiness(l))
				.summaryStatistics();

		System.err.println("max happiness is " + stats.getMax());

		FileIO.getFileAsStream("seating.txt").forEach(e -> processEntry(e, true));

		stats = Collections2.permutations(seatMap.keySet()).stream()
				.mapToInt(l -> computeHappiness(l))
				.summaryStatistics();

		System.err.println("max happiness with me is " + stats.getMax());

	}

	private static int computeHappiness(List<String> l) {
		int happiness = 0;
		for (int i = 0; i < (l.size() - 1); i++) {
			happiness += findHappiness(l.get(i), l.get(i+1));
			happiness += findHappiness(l.get(i+1), l.get(i));
		}
		happiness += findHappiness(l.get(l.size() -1), l.get(0));
		happiness += findHappiness(l.get(0), l.get(l.size() -1));
		return happiness;
	}

	private static int findHappiness(String s1, String s2) {
		return seatMap.get(s1).get(s2);
	}

	private static void processEntry(String s, boolean includeSelf) {
		String[] parts = s.split("\\s");
		if (parts.length == 11) {
			String from = parts[0], to = parts[10], direction = parts[2], points = parts[3];
			to = to.replace(".", "");
			Integer numPoints = Integer.parseInt(points);
			numPoints *= (direction.equals("gain") ? 1: -1);
			Map<String, Integer> entry = seatMap.get(from);
			if (entry == null) {
				entry = new HashMap<String, Integer>();
				seatMap.put(from, entry);
			}
			entry.put(to, numPoints);
			if (includeSelf) {
				entry.put("me", 0);

				entry = seatMap.get("me");
				if (entry == null) {
					entry = new HashMap<String, Integer>();
					seatMap.put("me", entry);
				}
				entry.put(from, 0);

			}
		}
	}
}

