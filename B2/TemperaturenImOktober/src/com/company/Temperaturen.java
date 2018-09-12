package com.company;

/**
 * Project: TemperaturenImOktober
 * Modul: 404
 * @author Marcelino Altamirano
 * @version 12.04.2018
 */

public class Temperaturen {
    public void initialise(double[] temps) {
        temps[0] = 19;
        temps[1] = 18;
        temps[2] = 17;
        temps[3] = 16;
        temps[4] = 16;
        temps[5] = 15;
        temps[6] = 15;
        temps[7] = 15;
        temps[8] = 14;
        temps[9] = 14;
        temps[10] = 16;
        temps[11] = 17;
        temps[12] = 17;
        temps[13] = 18;
        temps[15] = 17;
        temps[14] = 18;
        temps[16] = 17;
        temps[17] = 15;
        temps[18] = 14;
        temps[19] = 13;
        temps[20] = 12;
        temps[21] = 12;
        temps[22] = 11;
        temps[23] = 13;
        temps[24] = 18;
        temps[25] = 19;
        temps[26] = 17;
        temps[27] = 16;
        temps[28] = 16;
        temps[29] = 15;
        temps[30] = 15;

        zeilenweiseAusgebenMitFor(temps);
        minMax(temps);
        mittelwert(temps);
    }

    private void zeilenweiseAusgebenMitFor(double[] temps) {
        for (int i = 0; i < temps.length; i++) {
            System.out.println("Die Temperatur am " + i + ". Oktober war " + temps[i] + " Grad.");
        }
    }

    private double minimum(double[] temps) {
        double j = temps[0];
        for (int i = 0; i < temps.length; i++) {
            if (temps[i] < j) {
                j = temps[i];
            }
        }
        return j;
    }

    private double maximum(double[] temps) {
        double j = temps[0];
        for (int i = 0; i < temps.length; i++) {
            if (temps[i] > j) {
                j = temps[i];
            }
        }
        return j;
    }

    private void minMax(double[] temps) {
        System.out.println("Minimum: " + minimum(temps));
        System.out.println("Maximum: " + maximum(temps));
        System.out.println("Grösste Differenz: " + schrittweite(minimum(temps), maximum(temps)));
    }

    private double schrittweite(double min, double max) {
        return max - min;
    }

    private void mittelwert(double[] temps) {
        double sum = 0;

        for (int i = 0; i < temps.length; i++) {
            sum += temps[i];
        }
        System.out.println("Mittelwert: " + sum / temps.length);
    }
}