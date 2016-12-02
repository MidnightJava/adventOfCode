package aoc;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class AocDay04 {

	public static void main(String[] args) {
		md5Hash("00000");
		md5Hash("000000");
	}
	
	private static void md5Hash(String match) {
		String KEY_BASE = "ckczppom";
		int keySuffix = 1;
		try {
			MessageDigest md = MessageDigest.getInstance("MD5");
			while (!valid(md.digest((KEY_BASE + Integer.toString(keySuffix)).getBytes()), match)) {
				keySuffix++;
			}
			System.err.println("KEY FOUND: " + keySuffix);
		} catch (NoSuchAlgorithmException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static boolean valid(byte[] digest, String match) {
		StringBuilder sb = new StringBuilder();
		for(int i=0; i< digest.length ;i++)
		{
			sb.append(Integer.toString((digest[i] & 0xff) + 0x100, 16).substring(1));
		}

		return sb.toString().startsWith(match);
	}


}
