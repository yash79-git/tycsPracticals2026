package homePractise;

import java.util.Scanner;

public class railfenceKey2 {
    public static  String encryption(String plainText){
        StringBuffer cipher=new StringBuffer();
        for(int i=0;i<plainText.length();i+=2){
            cipher.append(plainText.charAt(i));
        }
        for(int i =1;i<plainText.length();i+=2){
            cipher.append(plainText.charAt(i));
        }
        return cipher.toString();

    }
    public static String decryption(String cipher){
        StringBuffer plainText=new StringBuffer();
        int mid=(cipher.length()+1)/2;
        for(int i=0;i<mid;i++){
            plainText.append(cipher.charAt(i));
            if(mid+i < cipher.length()){
                plainText.append(cipher.charAt(mid+i));
            }
        }
        return plainText.toString();
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter Plain Text : ");
        String plainText=sc.next();
        String cipher=encryption(plainText);
        System.out.println("Cipher Text : "+cipher);
        String decryptedText=decryption(cipher);
        System.out.println("Plain Text : "+decryptedText);
    }
}
