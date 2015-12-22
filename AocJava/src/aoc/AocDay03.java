package aoc;

import java.awt.Point;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.Charset;
import java.util.HashSet;
import java.util.Set;

public class AocDay03 {
	
	private static Set<Point> visited = new HashSet<Point>();
	private static Point currentPos;
	private static int currentSanta;
	private static Point[] positions = new Point[2];

	public static void main(String[] args) {
		try {
			;
			numHousesVisited(FileIO.getFileAsString("deliveryInput", Charset.defaultCharset()));
			numHousesVisited2(FileIO.getFileAsString("deliveryInput", Charset.defaultCharset()));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static void numHousesVisited(String line) throws IOException {
		visited = new HashSet<Point>();
		int token = 0;
		currentPos = new Point(0, 0);
		visited.add(new Point(0, 0));
		for (int i =0; i <line.length(); i++) {
			token = line.codePointAt(i);
			switch ((char) token) {
			case '^':
				visited.add(new Point(currentPos.x, currentPos.y + 1));
				currentPos.y = currentPos.y + 1;
				break;
			case '>':
				visited.add(new Point(currentPos.x + 1, currentPos.y));
				currentPos.x = currentPos.x + 1;
				break;
			case '<':
				visited.add(new Point(currentPos.x - 1, currentPos.y));
				currentPos.x = currentPos.x - 1;
				break;
			case 'v':
				visited.add(new Point(currentPos.x, currentPos.y - 1));
				currentPos.y = currentPos.y - 1;
				break;
			}
		}
		System.err.println("TOTAL Visited: " + visited.size());
	}

	private static void numHousesVisited2(String line) throws IOException {
		visited = new HashSet<Point>();
		int token = 0;
		positions[0] = new Point(0, 0);
		positions[1] = new Point(0, 0);
		currentSanta = 0;
		visited.add(new Point(0, 0));
		for (int i = 0; i < line.length(); i++) {
			token = line.codePointAt(i);
			switch ((char) token) {
			case '^':
				visited.add(new Point(positions[currentSanta].x, positions[currentSanta].y + 1));
				positions[currentSanta].y = positions[currentSanta].y + 1;
				break;
			case '>':
				visited.add(new Point(positions[currentSanta].x + 1, positions[currentSanta].y));
				positions[currentSanta].x = positions[currentSanta].x + 1;
				break;
			case '<':
				visited.add(new Point(positions[currentSanta].x - 1, positions[currentSanta].y));
				positions[currentSanta].x = positions[currentSanta].x - 1;
				break;
			case 'v':
				visited.add(new Point(positions[currentSanta].x, positions[currentSanta].y - 1));
				positions[currentSanta].y = positions[currentSanta].y - 1;
				break;
			}
			currentSanta = 1 - currentSanta;
		}
		System.err.println("TOTAL Visited (2 Santas): " + visited.size());
	}

}
