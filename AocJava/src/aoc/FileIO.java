package aoc;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.nio.charset.Charset;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

public class FileIO {

	public static Stream<String> getFileAsStream(String file) {
		try {
			return  Files.lines(FileSystems.getDefault().getPath(".", file));
		} catch (IOException e) {
			e.printStackTrace();
			return Arrays.stream(new String[0]);
		}
	}

	public static List<String> getFileAsList(String file) {
		try {
			return  Files.readAllLines(FileSystems.getDefault().getPath(".", file));
		} catch (IOException e) {
			e.printStackTrace();
			return new ArrayList<String>();
		}
	}

	static String getFileAsString(String file, Charset encoding) {
		byte[] encoded = null;
		try {
			encoded = Files.readAllBytes(FileSystems.getDefault().getPath(".", file));
			return new String(encoded, encoding);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return "";
		}
		
	}
}
