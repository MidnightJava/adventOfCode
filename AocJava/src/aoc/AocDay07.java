package aoc;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AocDay07 {

	private static HashMap<String, LogicExpression> gateMap;

	private static Map<String, Integer> resolvedMap = new HashMap<String, Integer>();

	public static void main(String[] args) {
		gates(false);
		gateMap = new HashMap<String, LogicExpression>();
		resolvedMap = new HashMap<String, Integer>();
		gates(true);
	}

	private static class LogicExpression {
		public String op;

		public Object operand1;

		public Object operand2;
	}

	private static void gates(boolean part2) {
		gateMap = new HashMap<String, LogicExpression>();
		try {
			gates(FileIO.getFileAsList("gates"), part2);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static void gates(List<String> lines, boolean part2) throws IOException {
		if (part2) {
			resolvedMap.put("b", 3176);
		}
		for (String line: lines) {
			parseGateLine(line);
		}
		LogicExpression l = gateMap.get("a");
		int output = eval(l);
		System.err.println("Logic output: " + output);
	}

	private static int eval(LogicExpression l) {
		Integer operand1 = null;
		Integer operand2 = null;
		if (l.operand1 instanceof String) {
			operand1 = resolvedMap.get(l.operand1);
			if (operand1 == null) {
				operand1 = eval(gateMap.get(l.operand1));
				resolvedMap.put((String) l.operand1, operand1);
			}
		} else {
			operand1 = (Integer) l.operand1;
		}
		if (l.operand2 instanceof String) {
			operand2 = resolvedMap.get(l.operand2);
			if (operand2 == null) {
				operand2 = eval(gateMap.get(l.operand2));
				resolvedMap.put((String) l.operand2, operand2);
			}
		} else {
			operand2 = (Integer) l.operand2;
		}
		if (l.op == null) {
			return operand2;
		}
		if (l.op.equals("NOT")){ 
			return ~operand2;
		} else if (l.op.equals("AND")){ 
			return operand1 & operand2;
		} else if (l.op.equals("OR")){ 
			return operand1 | operand2;
		} else if (l.op.equals("RSHIFT")){ 
			return operand1 >> operand2;
		} else if (l.op.equals("LSHIFT")){ 
			return operand1 << operand2;
		}
		throw new IllegalArgumentException("Cannot evaluate logic expression");
	}

	private static void parseGateLine(String line) {
		String regex = "([a-z]+\\s|[0-9]+\\s)*([A-Z]+\\s)*([a-z]+|[0-9]+)\\s\\-\\>\\s([a-z]+)";

		Pattern p = Pattern.compile(regex);
		Matcher m = p.matcher(line);
		if (m.matches()) {
			LogicExpression l = new LogicExpression();
			if (m.groupCount() == 4) {
				String g1 = m.group(1);
				if (g1 != null) {
					g1 = g1.trim();
				}
				try {
					l.operand1 = Integer.valueOf(g1);
				} catch (NumberFormatException e) {
					l.operand1 = g1;
				}
				String g3 = m.group(3).trim();
				try {
					l.operand2 = Integer.valueOf(g3);
				} catch (NumberFormatException e) {
					l.operand2 = g3;
				}
				String g2 = m.group(2);
				if (g2 != null) {
					g2 = g2.trim();
				}
				l.op = g2;
				StringBuilder sb = new StringBuilder();
				if (l.operand1 != null) {
					sb.append(l.operand1 + " ");
				}
				if (l.op != null) {
					sb.append(l.op + " ");
				}
				if (l.operand2 != null) {
					sb.append(l.operand2 + " ");
				}
				sb.append(" -> ");
				gateMap.put(m.group(4).trim(), l);
			} else {
				throw new IllegalArgumentException("Error parsing logic expression");
			}
		}
	}
}
