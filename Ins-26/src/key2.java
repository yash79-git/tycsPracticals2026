//package Ins.railfence;

import java.util.Scanner;

public class key2 {
    public static String railfence(String plainText){
        StringBuffer cipherext=new StringBuffer();
        for(int i=0;i<plainText.length();i+=2){
            cipherext.append(plainText.charAt(i));
        }
        for(int i=1;i<plainText.length();i+=2){
            cipherext.append(plainText.charAt(i));
        }
        return cipherext.toString();
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter Plain Text.");
        String plainText=sc.next();
        String cipher=railfence(plainText);
        System.out.println("Encrypted Text "+cipher);
    }
}
