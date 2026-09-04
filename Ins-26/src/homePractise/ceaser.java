package homePractise;

import java.util.Scanner;

public class ceaser {
    public static String encryption(String plainText,int key){
        StringBuffer cipher=new StringBuffer();
        for(int i =0;i<plainText.length();i++){
            char character;
            if(Character.isUpperCase(plainText.charAt(i))){
                character= (char) (((int)plainText.charAt(i) + key - 65) % 26 +65);
                cipher.append(character);
            }
            if(Character.isLowerCase(plainText.charAt(i))){
                character=(char)(((int)plainText.charAt(i)+ key - 97 )%26+97);
                cipher.append(character)
;            }
        }
        return cipher.toString();
    }
    public static String decryption(String cipherText,int key){
       StringBuffer plainText=new StringBuffer();
       char character;
       for(int i =0;i<cipherText.length();i++){
           if(Character.isUpperCase(cipherText.charAt(i))){
               character=(char)((int)(cipherText.charAt(i) - 65 - key + 26 )%26 +65);
               plainText.append(character);
           }
           if(Character.isLowerCase(cipherText.charAt(i))){
               character=(char)((int)(cipherText.charAt(i) - 97 - key + 26)%26 +97);
               plainText.append(character);
           }
       }
        return plainText.toString();
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter Plain Text : ");
        String plainText=sc.next();
        System.out.println("Enter Key : ");
        int key=sc.nextInt();
        String cipher=encryption(plainText,key);
        System.out.println("Cipher Text : "+cipher);
        String decryptedText=decryption(cipher,key);
        System.out.println("Plain Text : "+decryptedText);
    }
}
