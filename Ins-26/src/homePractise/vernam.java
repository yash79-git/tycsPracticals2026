package homePractise;

import java.util.Scanner;

public class vernam {
    public static String encryption(String plainText,String key){
        StringBuffer cipher=new StringBuffer();
        char character;
        for(int i=0;i<plainText.length();i++){
            character= (char) (plainText.charAt(i) ^ key.charAt(i));
            cipher.append(character);
        }
        return cipher.toString();
    }
    public static String decryption(String cipher,String key){
        char character;
        StringBuffer plainText=new StringBuffer();
        for(int i=0;i<cipher.length();i++){
            character= (char) (cipher.charAt(i) ^ key.charAt(i));
            plainText.append(character);
        }
        return plainText.toString();
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter Plain Text : ");
        String plainText=sc.next();
        System.out.println("Enter Key : ");
        String key=sc.next();
        if(!(key.length()==plainText.length())){
            System.out.println("Error : Key and Plain Text must have same Length. ");
            return;
        }
        String cipher=encryption(plainText,key);
        String decryptedText=decryption(cipher,key);
        System.out.println("Cipher Text : "+cipher);
        System.out.println("Plain Text : "+decryptedText);




    }
}
