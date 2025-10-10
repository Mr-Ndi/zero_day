package com.ndi.challenge1;

import java.util.Scanner;

public class reversePyramid {
    public static void main(String[] args) {
        Scanner injira = new Scanner(System.in);
        
        // Prompt for the number of rows
        System.out.print("Enter the number of rows (less than 10): ");
        int number = injira.nextInt();
        
        // Keep asking for input while the number is less than 10
        while (number < 10) {
            for (int njye = 1; njye <= number; njye++) {
                
                // Print spaces
                for (int woe = 1; woe < njye; woe++) {
                    System.out.print(" ");
                }
                
                // Print "@" symbols
                for (int ikirango = 1; ikirango <= (2 * (number - njye) + 1); ikirango++) {
                    System.out.print("@");
                }
                
                // Move to the next line after each row
                System.out.println();
            }
            
            // Ask for the number of rows again if the number was less than 10
            System.out.print("\nEnter a number of rows (less than 10): ");
            number = injira.nextInt();
        }
        
        // When the number is 10 or greater, print the message
        System.out.println("Poli yanze ko wageza 10 rows");

        // Close the scanner outside the loop
        injira.close();
    }
}
