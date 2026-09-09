//package inspractical;

import java.util.Scanner;

public class monoAlphabetic {
    public static String Encrypt(String plainText, String monoAplhaString) {
        StringBuffer sb = new StringBuffer(plainText);
        for (int i = 0; i < plainText.length(); i++) {
            int idx;
            char c;
            idx = plainText.charAt(i) - 65;
            c = monoAplhaString.charAt(idx);
            sb.setCharAt(i, c);
        }
        return (sb.toString());
    }

    public static String Decrpyt(String encrpytedText, String monoAplhaString) {
        StringBuffer sb = new StringBuffer(encrpytedText);
        int idx;
        char c;
        for (int i = 0; i < encrpytedText.length(); i++) {
            c = encrpytedText.charAt(i);
            idx = monoAplhaString.indexOf(c);
            char original = (char) (idx + 65);
            sb.setCharAt(i, original);
        }
        return (sb.toString());

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String monoString = "MNBVCXZLKJHGFDSAQWERTYUIOP";
        System.out.println("Monoalphabetic Program:");
        System.out.println("Enter Plain text : ");
        String s = sc.next();
        String e = Encrypt(s.toUpperCase(), monoString);
        System.out.println("Encrypted Text :" + e);
        String d = Decrpyt(e, monoString);
        System.out.println("Decrypted Text : " + d);

    }

}