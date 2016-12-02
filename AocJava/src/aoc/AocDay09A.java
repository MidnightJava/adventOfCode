package aoc;

import java.util.HashMap;
import java.util.IntSummaryStatistics;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collector;

import com.google.common.collect.Collections2;

public class AocDay09A {
	
	public static void main(String[] args) {

		IntSummaryStatistics stats = FileIO.getFileAsStream("input-9.txt") //stream
				.map(s -> parseEntry(s))
				.collect(Collector.of(
						HashMap::new, (m1,m2) -> mergeMaps(m1, m2), (t, u) -> t, finish)); //combiner is NOOP

		System.err.println("min value is " + stats.getMin());
		System.err.println("max value is " + stats.getMax());

	}

	private static Map<String, Map<String, Integer>> parseEntry(String s) {
		HashMap<String, Map<String, Integer>> routes = new HashMap<String, Map<String, Integer>>();
		String[] parts = s.split("\\s");
		if (parts.length == 5) {
			String from = parts[0], to = parts[2], dist = parts[4];
			Map<String, Integer> entry = new HashMap<String, Integer>();
			entry.put(to, new Integer(dist));
			routes.put(from, entry);
			entry = new HashMap<String, Integer>();
			entry.put(from, new Integer(dist));
			routes.put(to, entry);
			return routes;
		} else {
			throw new IllegalArgumentException("Invalid input record");
		}
	}


	private static Map<String, Map<String, Integer>> mergeMaps(Map<String, Map<String, Integer>> container, Map<String, Map<String, Integer>> element) {
		for (String key : element.keySet()) {
			Map<String, Integer> entry = container.get(key);
			if (entry == null) {
				entry = new HashMap<String, Integer>();
				container.put(key, entry);
			}
			entry.putAll(element.get(key));
		}
		return container;
	}

	private static Function<Map<String, Map<String, Integer>>, IntSummaryStatistics> finish
	= new Function<Map<String, Map<String, Integer>>, IntSummaryStatistics>() {

		@Override
		public IntSummaryStatistics apply(Map<String, Map<String, Integer>> routes) {
			return Collections2.permutations(routes.keySet()).stream()
					.mapToInt(l -> computeDistance(routes, l))
					.summaryStatistics();
		}

	};

	private static int computeDistance(Map<String, Map<String, Integer>> routes, List<String> l) {
		int distance = 0;
		for (int i = 0; i < (l.size() - 1); i++) {
			distance += routes.get(l.get(i)).get(l.get(i+1));
		}
		return distance;
	}

}
