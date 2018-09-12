package com.company;

/**
 * Project: Zahlensysteme
 * Modul: 404
 * @author Marcelino Altamirano
 * @version 08.03.2018
 */

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input;
        String number;
        int system;
        do {
            System.out.println("==============================");
            System.out.println("What do you want to calculate?");
            System.out.println("==============================");
            System.out.println("1) Decimal to any System");
            System.out.println("2) Any System to Decimal");
            System.out.println("0) End");
            System.out.println("==============================");
            System.out.print("Choice: ");
            input = scanner.nextLine();
            System.out.println("==============================");

            switch (input) {
                case "1":
                    System.out.print("Number: ");
                    number = scanner.nextLine();
                    System.out.print("To which System: ");
                    system = Integer.parseInt(scanner.nextLine());
                    System.out.println(number + " in " + system + "-System: "  + decTo(Integer.parseInt(number), system));
                    break;
                case "2":
                    System.out.print("Number: ");
                    number = scanner.nextLine();
                    System.out.print("From which System: ");
                    system = Integer.parseInt(scanner.nextLine());
                    System.out.println(number + " in Decimal: " + toDec(number, system));
                    break;
                default:
            }
        } while (!input.equals("0"));
    }

    private static String decTo(int number, int system) {
        StringBuilder binNumber = new StringBuilder();
        int i = 0;
        int y;

        // Es wird berechnet wie viele Stellen die Zahl braucht
        while (Math.pow(system, i) < number) {
            i++;
        }

        // Um die Abstände richtig zu setzten
        int addSpace = 0;

        while ((i + addSpace) % 4 != 0) {
            addSpace++;
        }

        //  Um überflüssige 0en zu eliminieren
        if (Math.pow(system, i) != number) {
            i--;
        }

        // Einzelne Stellen berechnen
        for (int j = i; j >= 0; j--) {
            y = 0;
            while (number - Math.pow(system, j) >= 0) {
                y++;
                number -= Math.pow(system, j);
            }

            switch (y) {
                case 10:
                    binNumber.append("A");
                    break;
                case 11:
                    binNumber.append("B");
                    break;
                case 12:
                    binNumber.append("C");
                    break;
                case 13:
                    binNumber.append("D");
                    break;
                case 14:
                    binNumber.append("E");
                    break;
                case 15:
                    binNumber.append("F");
                    break;
                case 16:
                    binNumber.append("G");
                    break;
                case 17:
                    binNumber.append("H");
                    break;
                case 18:
                    binNumber.append("I");
                    break;
                case 19:
                    binNumber.append("J");
                    break;
                default:
                    binNumber.append(y);
            }

            // Prüft ob ein Abstand hinkommt
            if ((binNumber.length() + addSpace) % 4 == 0) {
                binNumber.append(" ");
                addSpace--;
            }
        }

        return binNumber.toString();
    }

    private static int toDec(String number, int system) {
        int decNumber = 0;
        int index = number.length() - 1;
        int digit;
        number = number.toLowerCase();

        // Es wird durch jede Stelle iteriert, welche dann multipliziert wird
        for (int i = 0; i < number.length(); i++) {
            switch (number.charAt(index)) {
                case 'a':
                    digit = 10;
                    break;
                case 'b':
                    digit = 11;
                    break;
                case 'c':
                    digit = 12;
                    break;
                case 'd':
                    digit = 13;
                    break;
                case 'e':
                    digit = 14;
                    break;
                case 'f':
                    digit = 15;
                    break;
                case 'g':
                    digit = 16;
                    break;
                case 'h':
                    digit = 17;
                    break;
                case 'i':
                    digit = 18;
                    break;
                case 'j':
                    digit = 19;
                    break;
                default:
                    digit = Character.getNumericValue(number.charAt(index));
            }
            decNumber += digit * Math.pow(system, i);
            index--;
        }
        return decNumber;
    }
}
