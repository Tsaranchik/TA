import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

import static java.lang.System.exit;

public class Graph {
    private static boolean[] x = new boolean[16];
    private static boolean[] y = new boolean[26];

    private static void readXFromFile(String fileName) throws IOException {
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line = br.readLine();

            if (line == null)
                throw new IOException("\nInvalid input: Not enough data in file.");

            String[] lineArr = line.split(" ");
            for (int i = 1; i < x.length; ++i) {
                if (!lineArr[i - 1].equals("0") && !lineArr[i - 1].equals("1"))
                    throw new IOException("\nInvalid input: Only 0 and 1 are allowed.");

                x[i] = lineArr[i - 1].equals("1");
            }
        }
    }

    private static void displayHeader() {
        System.out.print("     ");
        for (int i = 1; i <= 25; ++i) {
            System.out.printf("y%-2d ", i);
        }
        System.out.println();
    }

    private static void displayState(int state) {
        System.out.printf("S%-2d   ", state);
        for (int i = 1; i <= 25; ++i) {
            System.out.print(y[i] ? "1   " : "0   ");
        }
        System.out.println();
    }

    private static void clearYArray() {
        Arrays.fill(y, false);
    }

    public static void run() {
        long startTime = System.currentTimeMillis();
        try {
            readXFromFile("input.txt");

        } catch (IOException e) {
            System.err.println(e.getMessage());
            exit(1);
        }

        Arrays.fill(y, false);

        int step = 0;
        int state = 0;
        displayHeader();
        displayState(state);

        while (step < 20) {
            if (state == 0) {
                if (!x[1] && !x[2] && !x[4] && !x[5] ||
                    !x[1] && x[2] && !x[3] && !x[4] && !x[5]) {
                    state = 1;
                    y[1] = true; y[2] = true; y[3] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                if (!x[1] && !x[2] && !x[4] && x[5] ||
                    !x[1] && x[2] && !x[3] && !x[4] && x[5]) {
                    state = 2;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                if (x[1] && !x[12] ||
                    !x[1] && !x[2] && x[4] && !x[6] && !x[12] ||
                    !x[1] && x[2] && !x[3] && x[4] && !x[6] && x[12]) {
                    state = 4;
                    y[5] = true; y[6] = true; y[7] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                if (x[1] && x[12] && x[13] ||
                    !x[1] && !x[2] && x[4] && !x[6] && x[12] && x[13] ||
                    !x[1] && x[2] && !x[3] && x[4] && !x[6] && x[12] && x[13]) {
                    state = 5;
                    y[20] = true; y[21] = true; y[18] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                if (x[1] && x[12] && !x[13] && x[1] ||
                    !x[1] && !x[2] && x[4] && !x[6] && x[12] && !x[13] && x[1] ||
                    !x[1] && x[2] && !x[3] && x[4] && !x[6] && x[12] && !x[13] && x[1]) {
                    state = 6;
                    y[1] = true; y[2] = true; y[15] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                if (!x[1] && x[2] && x[3] ||
                    !x[1] && !x[2] && x[4] && x[6] ||
                    !x[1] && x[2] && !x[3] && x[4] && x[6]) {
                    state = 7;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                if (x[1] && x[12] && !x[13] && !x[1] ||
                    !x[1] && !x[2] & x[4] && !x[6] && x[12] && !x[13] && !x[1] ||
                    !x[1] && x[2] && !x[3] && x[4] && !x[6] && x[12] && !x[13] && !x[1]) {
                    state = 8;
                    y[21] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }
            }

            else if (state == 1) {
                if (!x[9]) {
                    state = 1;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                else {
                    state = 2;
                    y[4] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }
            }

            else if (state == 2) {
                if (x[10] && x[11] && x[7]) {
                    state = 3;
                    y[5] = true; y[8] = true; y[9] = true; y[7] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                if (!x[10] && !x[12] ||
                    x[10] && !x[11] ||
                    x[10] && x[11] && !x[7]) {
                    state = 4;
                    y[5] = true; y[6] = true; y[7] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                if (!x[10] && x[12] && x[13]) {
                    state = 5;
                    y[16] = true; y[21] = true; y[18] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                if (x[1] && x[12] && !x[13] && !x[1]) {
                    state = 6;
                    y[1] = true; y[2] = true; y[15] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                if (!x[10] && x[12] && !x[13] && !x[1]) {
                    state = 8;
                    y[21] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }
            }

            else if (state == 3) {
                if (!x[14]) {
                    state = 3;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                else {
                    state = 7;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }
            }

            else if (state == 4) {
                if (!x[15]) {
                    state = 4;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                if (x[15] && !x[11] ||
                    x[15] && x[11] && !x[13] && !x[1] && !x[10]) {
                    state = 2;
                    y[10] = true; y[11] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                if (x[15] && x[11] && x[13]) {
                    state = 5;
                    y[20] = true; y[17] = true; y[18] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                if (x[15] && x[11] && !x[13] && x[1]) {
                    state = 6;
                    y[1] = true; y[19] = true; y[15] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                if (x[15] && x[11] && !x[13] && !x[1] && x[10]) {
                    state = 7;
                    y[23] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }
            }

            else if (state == 5) {
                if (!x[8]) {
                    state = 5;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                if (x[8] && x[7]) {
                    state = 3;
                    y[5] = true; y[13] = true; y[9] = true; y[7] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                else {
                    state = 7;
                    y[12] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }
            }

            else if (state == 6) {
                if (!x[9]) {
                    state = 6;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                else {
                    state = 7;
                    y[14] = true;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }
            }

            else if (state == 7) {
                state = 8;
                y[22] = true;
                displayState(state);
                clearYArray();
                step++;
                continue;
            }

            else if (state == 8) {
                state = 9;
                y[24] = true; y[6] = true; y[7] = true;
                displayState(state);
                clearYArray();
                step++;
                continue;
            }

            else if (state == 9) {
                if (!x[15]) {
                    state = 9;
                    displayState(state);
                    clearYArray();
                    step++;
                    continue;
                }

                else {
                    state = 0;
                    y[25] = true;
                    displayState(state);
                    clearYArray();
                    System.out.println("The programme ended!");
                    break;
                }
            }

            clearYArray();
            step++;
        }
        if (step >= 20) {
            System.out.println("The programme looped!");
        }
        long endTime = System.currentTimeMillis();
        System.out.printf("Runtime: %d ms\n\n", endTime - startTime);
    }
}
