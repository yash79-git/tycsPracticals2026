package homePractise;

import java.util.Scanner;

public class monoAlphabetic {
    public static String encryption(String plainText,String monoAlphabeticString){
        StringBuffer cipher=new StringBuffer("yash");
        for(int i =0;i<plainText.length();i++){
            int asciiValue=plainText.charAt(i)-65;
            char charInMonoAlphaString=monoAlphabeticString.charAt(asciiValue);
            cipher.setCharAt(i,charInMonoAlphaString);
        }
        return cipher.toString();

    }
    public static String decryption(String cipherText,String monoAlphabeticString){
        StringBuffer plainText=new StringBuffer("yash");
        for(int i=0;i<cipherText.length();i++){
            int indexInMonoAlphaString=monoAlphabeticString.indexOf(cipherText.charAt(i));
            int originalCharAscii=indexInMonoAlphaString+65;
            plainText.setCharAt(i,(char) originalCharAscii);
        }
        return plainText.toString();

    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String monoAlphabeticString="qwertyuioplkjhgfdsazxcvbnm";
        System.out.println("Enter Plain Text");
        String plainText=sc.next();
//        boolean isUpper=false;
        String cipher=encryption(plainText.toUpperCase(),monoAlphabeticString);
        System.out.println("Cipher Text : "+cipher);
        String decryptedText=decryption(cipher,monoAlphabeticString);
        System.out.println("Plain Text : "+decryptedText);

    }
}
