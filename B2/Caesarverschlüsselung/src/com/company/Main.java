package com.company;

/**
 * Project: Caesarverschluesselung
 * Modul: 404
 * @author Marcelino Altamirano
 * @version 05.07.2018
 */

import java.util.Scanner;

public class Main {
    private char[] abc = {
            'a',
            'b',
            'c',
            'd',
            'e',
            'f',
            'g',
            'h',
            'i',
            'j',
            'k',
            'l',
            'm',
            'n',
            'o',
            'p',
            'q',
            'r',
            's',
            't',
            'u',
            'v',
            'w',
            'x',
            'y',
            'z'
    };

    public static void main(String[] args) {
        Main main = new Main();
        main.start();
    }

    private void start() {
        Scanner scanner = new Scanner(System.in);
        StringBuilder solution = new StringBuilder();
        char[] code = scanner.nextLine().toLowerCase().toCharArray();
        int difference = Integer.parseInt(scanner.nextLine());
        for (char aCode : code) {
            if (inArray(aCode)) {
                solution.append(abc[getCorrectNumber(index(aCode) + difference)]);
            } else {
                solution.append(aCode);
            }
        }
        System.out.println(solution);
    }

    private int index(char c) {
        for (int i = 0; i < abc.length; i++) {
            if (c == abc[i]) {
                return i;
            }
        }
        return 0;
    }

    private boolean inArray(char c) {
        for (char anAbc : abc) {
            if (c == anAbc) {
                return true;
            }
        }
        return false;
    }

    private int getCorrectNumber(int i) {
        while (i < 0 || i > 25) {
            if (i < 0)
                i += 26;
            else
                i -= 26;
        }
        return i;
    }
}