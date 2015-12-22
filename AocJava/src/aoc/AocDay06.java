package aoc;

import java.awt.Rectangle;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class AocDay06 {
	
	private static boolean[][] grid = new boolean[1000][1000];

	private static int[][] grid2 = new int[1000][1000];

	public static void main(String[] args) {
		lights();
	}
	
	private static void lights() {
		for (boolean[] row : grid) {
			for (boolean light: row) {
				light = false;
			}
		}
		for (int[] row : grid2) {
			for (int light: row) {
				light = 0;
			}
		}
		try {
			lights(FileIO.getFileAsList("lights"));
			lights2(FileIO.getFileAsList("lights"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static  void lights(List<String> lines) throws IOException {
		for (String line: lines) {
			if (!line.trim().equals("")) {
				LightCommand command = parseCommand(line);
				switch (command.action) {
				case TOGGLE:
					for (int x = command.range.x; x <= (command.range.x + command.range.width); x++) {
						for (int y = command.range.y; y <= (command.range.y + command.range.height); y++) {
							if (grid[x][y] == true) {
								grid[x][y] = false;
							} else {
								grid[x][y] = true;
							}
						}
					}
					break;
				case TURN_OFF:
					for (int x = command.range.x; x <= (command.range.x + command.range.width); x++) {
						for (int y = command.range.y; y <= (command.range.y + command.range.height); y++) {
							grid[x][y] = false;
						}
					}
					break;
				case TURN_ON:
					for (int x = command.range.x; x <= (command.range.x + command.range.width); x++) {
						for (int y = command.range.y; y <= (command.range.y + command.range.height); y++) {
							grid[x][y] = true;
						}
					}
					break;
				}
			}
		}
		int count = 0;
		for (boolean[] row : grid) {
			for (boolean light: row) {
				if (light) {
					count++;
				}
			}
		}
		System.err.println("Number of Lights On: " + count);
	}

	private static void lights2(List<String> lines) throws IOException {
		for (String line: lines) {
			if (!line.trim().equals("")) {
				LightCommand command = parseCommand(line);
				switch (command.action) {
				case TOGGLE:
					for (int x = command.range.x; x <= (command.range.x + command.range.width); x++) {
						for (int y = command.range.y; y <= (command.range.y + command.range.height); y++) {
							grid2[x][y] = grid2[x][y] + 2;
						}
					}
					break;
				case TURN_OFF:
					for (int x = command.range.x; x <= (command.range.x + command.range.width); x++) {
						for (int y = command.range.y; y <= (command.range.y + command.range.height); y++) {
							if (grid2[x][y] > 0) {
								grid2[x][y] = grid2[x][y] - 1;
							}
						}
					}
					break;
				case TURN_ON:
					for (int x = command.range.x; x <= (command.range.x + command.range.width); x++) {
						for (int y = command.range.y; y <= (command.range.y + command.range.height); y++) {
							grid2[x][y] = grid2[x][y] + 1;
						}
					}
					break;
				}
			}
		}
		int brightness = 0;
		for (int[] row : grid2) {
			for (int light: row) {
				brightness+= light;
			}
		}
		System.err.println("Total brightness of lights: " + brightness);
	}

	private static LightCommand parseCommand(String line) {
		String regex = "([^\\d]+)\\s*(\\d+),(\\d+)\\s*through\\s*(\\d+),(\\d+)";
		Pattern p = Pattern.compile(regex);
		Matcher m = p.matcher(line);
		if (m.matches()) {
			LightAction action = LightAction.fromString(m.group(1).trim());
			Rectangle range = new Rectangle(Integer.valueOf(m.group(2)),
					Integer.valueOf(m.group(3)),
					Integer.valueOf(m.group(4)) - Integer.valueOf(m.group(2)),
					Integer.valueOf(m.group(5)) - Integer.valueOf(m.group(3)));
			LightCommand command = new LightCommand();
			command.range = range;
			command.action = action;
			return command;
		}
		return null;
	}
	
	private static enum LightAction {
		TURN_ON,
		TURN_OFF,
		TOGGLE;

		public static LightAction fromString(String action) {
			if (action.equals("turn on")) {
				return TURN_ON;
			} else if (action.equals("turn off")) {
				return TURN_OFF;
			} else if (action.equals("toggle")) {
				return TOGGLE;
			}
			return null;
		}
	}

	private static class LightCommand {
		Rectangle range;

		LightAction action;
	}

}
