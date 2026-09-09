import java.util.*;
public class CipherText {
    public static StringBuffer encrption(String plainText, int key) {
        // store encrypted text
        StringBuffer result = new StringBuffer();
        for (int i = 0; i < plainText.length(); i++) {
            // check very character is uppercase
            if (Character.isUpperCase(plainText.charAt(i))) {
                // perform encrption calculation for each character and append to result
                // varaible
                // 65 for uppercase
                char ch = (char) (((int) plainText.charAt(i) + key - 65) % 26 + 65);
                result.append(ch);
            } else {
                // 97 for lowecase
                char ch = (char) (((int) plainText.charAt(i) + key - 97) % 26 + 97);
                result.append(ch);
            }
        }
        return result;

    }

    public static StringBuffer decryption(String encrptedText, int key) {
        StringBuffer result = new StringBuffer();
        for (int i = 0; i < encrptedText.length(); i++) {
            // check uppercase
            if (Character.isUpperCase(encrptedText.charAt(i))) {
                // perform decryption calculation for each character and append to result
                // varaible
                // 65 for uppercase
                char ch = (char) ((((int) encrptedText.charAt(i) - 65 - key + 26) % 26) + 65);
                result.append(ch);
            } else {
                // 97 for lowercase
                char ch = (char) ((((int) encrptedText.charAt(i) - 97 - key + 26) % 26) + 97);
                result.append(ch);
            }
        }
        return result;

    }

    public static void main(String[] args) {
        System.out.println("Cipher Text Program.");
        Scanner sc = new Scanner(System.in);
        System.out.println("Input Plain Text");
        String input = sc.next();
        System.out.println("Enter Key.");
        int k = sc.nextInt();
        StringBuffer enc = encrption(input, k);
        StringBuffer dec = decryption(enc.toString(), k);
        System.out.println("Encrpted Text = " + enc);
        System.out.println("Decrypted Text = " + dec);
        sc.close();

    }

}