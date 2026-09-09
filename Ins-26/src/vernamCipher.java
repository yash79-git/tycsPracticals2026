import java.util.*;

public class vernamCipher {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter Plain Text : ");
        String plainText = sc.next();

        System.out.println("Enter Key : ");
        String key = sc.next();

        if (plainText.length() != key.length()) {
            System.out.println("Error: Plain text length and key length must be same.");
            return;
        }

        StringBuffer cipher = new StringBuffer();
        StringBuffer decrypt = new StringBuffer();

        // Encryption
        for (int i = 0; i < plainText.length(); i++) {
            char c = (char)(plainText.charAt(i) ^ key.charAt(i));
            cipher.append(c);

            // Display ASCII/Unicode value of cipher character
            System.out.println((int)c);
        }

        // Decryption
        for (int i = 0; i < cipher.length(); i++) {
            char p = (char)(cipher.charAt(i) ^ key.charAt(i));
            decrypt.append(p);
        }

        System.out.println("Cipher Text : " + cipher);
        System.out.println("Decrypted Text : " + decrypt);
    }
}