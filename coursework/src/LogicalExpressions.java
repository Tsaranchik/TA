import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

import static java.lang.System.exit;

public class LogicalExpressions {
    private static boolean[] x = new boolean[16];
    private static boolean[] a = new boolean[5];
    private static boolean[] y = new boolean[26];

    static void readXFromFile(String fileName) throws IOException {
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

    private static boolean w1() {
        return !a[1] && !a[2] && !a[3] && !a[4] &&
                ((!x[1] && !x[2] && x[4] && !x[6] && x[12] && !x[13] && !x[1])
                        || (!x[1] && x[2] && !x[3] && x[4] && !x[6] && x[12] && !x[13] && !x[1]))
                || (!a[1] && !a[2] && a[3] && !a[4] && !x[10] && x[12] && !x[13] && !x[1])
                || (!a[1] && a[2] && a[3] && a[4]);
    }

    private static boolean w2() {
        return !a[1] && !a[2] && !a[3] && !a[4]
                && (x[1] && !x[12] || !x[1] && !x[2] && x[4] && !x[6] && !x[12]
                || !x[1] && x[2] && !x[3] && x[4] && !x[6] && !x[12]
                || x[1] && x[12] && x[13]
                || !x[1] && !x[2] && x[4] && !x[6] && x[12] && x[13]
                || !x[1] && x[2] && !x[3] && x[4] && !x[6] && x[12] && x[13]
                || x[1] && x[12] && !x[13] && x[1]
                || !x[1] && x[2] && x[3]
                || !x[1] && !x[2] && x[4] && x[6]
                || !x[1] && x[2] && !x[3] && x[4] && x[6])
                || (!a[1] && !a[2] && a[3] && !a[4] && (!x[10] && !x[12] || x[10] && !x[11]
                || x[10] && x[11] && !x[7]
                || !x[10] && x[12] && x[13]))
                || (!a[1] && !a[2] && a[3] && a[4] && x[14]);

    }

    private static boolean w3() {
        return (!a[1] && !a[2] && !a[3] && !a[4] &&
                ((!x[1] && !x[2] && !x[4] && x[5]) ||
                        (!x[1] && !x[2] && !x[3] && !x[4] && x[5]) ||
                        (x[1] && x[12] && !x[13] && x[1]) ||
                        (!x[1] && x[2] && x[3]) ||
                        (!x[1] && !x[2] && x[4] && x[6]) ||
                        (!x[1] && x[2] && !x[3] && x[4] && x[6]))) ||
                (!a[1] && !a[2] && !a[3] && a[4] && x[9]) ||
                (!a[1] && a[2] && !a[3] && !a[4] &&
                        ((x[15] && !x[11]) ||
                                (x[15] && x[11] && !x[13] && !x[1] && !x[10]) ||
                                (x[15] && x[11] && !x[13] && x[1]) ||
                                (x[15] && x[11] && !x[13] && !x[1] && x[10]))) ||
                (!a[1] && a[2] && !a[3] && a[4] &&
                        ((x[8] && x[7]) ||
                                (x[8] && !x[7])));
    }

    private static boolean w4() {
        return (!a[1] && !a[2] && !a[3] && !a[4] &&
                ((!x[1] && !x[2] && !x[4] && !x[5]) ||
                        (!x[1] && x[2] && !x[3] && !x[4] && !x[5]) ||
                        (x[1] && x[12] && x[13]) ||
                        (!x[1] && !x[2] && x[4] && !x[6] && x[12] && x[13]) ||
                        (!x[1] && x[2] && !x[3] && x[4] && !x[6] && x[12] && x[13]) ||
                        (!x[1] && x[2] && x[3]) ||
                        (!x[1] && !x[2] && x[4] && x[6]) ||
                        (!x[1] && x[2] && !x[3] && x[4] && x[6]))) ||
                (!a[1] && !a[2] && a[3] && !a[4] &&
                        ((!x[10] && x[12] && x[13]) ||
                                (x[10] && x[11] && x[7]))) ||
                (!a[1] && a[2] && !a[3] && !a[4] &&
                        ((x[15] && x[11] && x[13]) ||
                                (x[15] && x[11] && !x[13] && !x[1] && x[10]))) ||
                (!a[1] && a[2] && a[3] && !a[4] && x[9]) ||
                (a[1] && !a[2] && !a[3] && !a[4]);
    }

    private static boolean u1() {
        return a[1] && !a[2] && !a[3] && a[4] && x[15];
    }

    private static boolean u2() {
        return !a[1] && a[2] && !a[3] && !a[4] && (x[15] && !x[11] ||
                x[15] && x[11] && !x[13] && !x[1] && !x[10]) ||
                (!a[1] && a[2] && a[3] && a[4]) ||
                (!a[1] && a[2] && !a[3] && a[4] && x[8] && x[7]);
    }


    private static boolean u3() {
        return !a[1] && !a[2] && a[3] && !a[4] && (!x[10] && !x[12] ||
                x[10] && !x[11] ||
                x[10] && x[11] && !x[7] ||
                !x[10] && x[12] && x[13] ||
                !x[10] && x[12] && !x[13] && !x[1]) ||
                (!a[1] && a[2] && a[3] && a[4]);
    }

    private static boolean u4() {
        return !a[1] && !a[2] && !a[3] && a[4] && x[9] ||
                !a[1] && a[2] && a[3] && a[4] ||
                a[1] && !a[2] && !a[3] && a[4] && x[15];
    }

    private static void calculateOutputs() {
        y[1] = !a[1] && !a[2] && !a[3] && !a[4] &&
                ((!x[1] && !x[2] && !x[4] && !x[5]) ||
                        (!x[1] && x[2] && !x[3] && !x[4] && !x[5]) ||
                        (x[1] && x[12] && !x[13] && x[1])) ||
                (!a[1] && a[2] && !a[3] && !a[4] && x[15] && x[11] && !x[13] && x[1]);

        y[2] = !a[1] && !a[2] && !a[3] && !a[4] &&
                ((!x[1] && !x[2] && !x[4] && !x[5]) ||
                        (!x[1] && x[2] && !x[3] && !x[4] && !x[5]) ||
                        (x[1] && x[12] && !x[13] && x[1]));

        y[3] = !a[1] && !a[2] && !a[3] && !a[4] &&
                ((!x[1] && !x[2] && !x[4] && !x[5]) ||
                        (!x[1] && x[2] && !x[3] && !x[4] && !x[5]));

        y[4] = !a[1] && !a[2] && !a[3] && a[4] && x[9];

        y[5] = !a[1] && !a[2] && !a[3] && !a[4] &&
                (x[1] && !x[12] ||
                        !x[1] && !x[2] && x[4] && !x[6] && !x[12] ||
                        !x[1] && x[2] && !x[3] && x[4] && !x[6] && !x[12]) ||
                (!a[1] && !a[2] && a[3] && !a[4] && (!x[10] && !x[11] && x[7] ||
                        !x[10] && !x[12] ||
                        x[10] && !x[11] ||
                        x[10] && x[11] && !x[7])) ||
                (!a[1] && a[2] && !a[3] && a[4] && x[8] && x[7]);

        y[6] = !a[1] && !a[2] && !a[3] && !a[4] &&
                (x[1] && !x[12] ||
                        !x[1] && !x[2] && x[4] && !x[6] && !x[12] ||
                        !x[1] && x[2] && !x[3] && x[4] && !x[6] && !x[12]) ||
                (!a[1] && !a[2] && a[3] && !a[4] && (!x[10] && !x[12] ||
                        x[10] && !x[11] ||
                        x[10] && x[11] && !x[7])) ||
                (a[1] && !a[2] && !a[3] && !a[4]);

        y[7] = !a[1] && !a[2] && !a[3] && !a[4] &&
                (x[1] && !x[12] ||
                        !x[1] && !x[2] && x[4] && !x[6] && !x[12] ||
                        !x[1] && x[2] && !x[3] && x[4] && !x[6] && !x[12]) ||
                (!a[1] && !a[2] && a[3] && !a[4] &&
                        (x[10] && x[11] && x[7] ||
                                !x[10] && !x[12] ||
                                x[10] && !x[11] ||
                                x[10] && x[11] && !x[7])) ||
                (!a[1] && a[2] && !a[3] && a[4] && x[8] && x[7]) ||
                (a[1] && !a[2] && !a[3] && !a[4]);

        y[8] = !a[1] && !a[2] && a[3] && !a[4] && x[10] && x[11] && x[7];

        y[9] = !a[1] && !a[2] && a[3] && !a[4] && x[10] && x[11] && x[7] ||
                !a[1] && a[2] && !a[3] && a[4] && x[8] && x[7];

        y[10] = !a[1] && a[2] && !a[3] && !a[4] &&
                (x[15] && !x[11] ||
                        x[15] && x[11] && !x[13] && !x[1] && !x[10]);

        y[11] = y[10];

        y[12] = !a[1] && a[2] && !a[3] && a[4] && x[8] && !x[7];

        y[13] = !a[1] && a[2] && !a[3] && a[4] && x[8] && x[7];

        y[14] = !a[1] && a[2] && a[3] && !a[4] && x[9];

        y[15] = !a[1] && !a[2] && !a[3] && !a[4] && x[1] && x[12] && !x[13] && x[1] ||
                !a[1] && a[2] && !a[3] && !a[4] && x[15] && x[11] && !x[13] && x[1];

        y[16] = !a[1] && !a[2] && a[3] && !a[4] && !x[10] && x[12] && x[13];

        y[17] = !a[1] && a[2] && !a[3] && !a[4] && x[15] && x[11] && x[13];

        y[18] = !a[1] && !a[2] && !a[3] && !a[4] &&
                ((x[1] && x[12] && x[13]) ||
                        (!x[1] && !x[2] && x[4] && !x[6] && x[12] && x[13]) ||
                        (!x[1] && x[2] && !x[3] && x[4] && !x[6] && x[12] && x[13])) ||
                !x[10] && x[12] && x[13] && !a[1] && !a[2] && a[3] && !a[4] ||
                x[15] && x[11] && x[13] && !a[1] && a[2] && !a[3] && !a[4];

        y[19] = !a[1] && a[2] && !a[3] && !a[4] && x[15] && x[11] && !x[13] && x[1];

        y[20] = !a[1] && !a[2] && !a[3] && !a[4] &&
                ((x[1] && x[12] && x[13]) ||
                        (!x[1] && !x[2] && x[4] && !x[6] && x[12] && x[13]) ||
                        (!x[1] && x[2] && !x[3] && x[4] && !x[6] && x[12] && x[13])) ||
                x[15] && x[11] && x[13] && !a[1] && a[2] && !a[3] && !a[4];

        y[21] = !a[1] && !a[2] && !a[3] && !a[4] &&
                ((x[1] && x[12] && x[13]) ||
                        (!x[1] && !x[2] && x[4] && !x[6] && x[12] && x[13]) ||
                        (!x[1] && x[2] && !x[3] && x[4] && !x[6] && x[12] && x[13]) ||
                        (!x[1] && !x[2] && x[4] && !x[6] && x[12] && !x[13] && !x[1])) ||
                !a[1] && !a[2] && a[3] && !a[4] &&
                        ((!x[10] && x[12] && x[13]) ||
                                (!x[10] && x[12] && !x[13] && !x[1]));

        y[22] = !a[1] && a[2] && a[3] && a[4];

        y[23] = !a[1] && a[2] && !a[3] && !a[4] && x[15] && x[11] && !x[13] && !x[1] && x[10];

        y[24] = a[1] && !a[2] && !a[3] && !a[4];

        y[25] = a[1] && !a[2] && !a[3] && a[4] && x[15];
    }

    private static boolean[] calculateNextState() {
        boolean set1 = false;
        boolean set2 = false;
        boolean set3 = false;
        boolean set4 = false;
        boolean[] tmp = a.clone();

        if (w1()) {
            tmp[1] = true;
            set1 = true;
        }

        if (w2()) {
            tmp[2] = true;
            set2 = true;
        }

        if (w3()) {
            tmp[3] = true;
            set3 = true;
        }

        if (w4()) {
            tmp[4] = true;
            set4 = true;
        }

        if (u1() && !set1){
            tmp[1] = false;
        }

        if (u2() && !set2){
            tmp[2] = false;
        }

        if (u3() && !set3){
            tmp[3] = false;
        }

        if (u4() && !set4) {
            tmp[4] = false;
        }

        return tmp;

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

    public static void run() {
        long startTime = System.currentTimeMillis();
        try {
            readXFromFile("input.txt");

        } catch (IOException e) {
            System.err.println(e.getMessage());
            exit(1);
        }

        Arrays.fill(a, false);

        int step = 0;
        displayHeader();
        displayState(0);

        while (true) {
            calculateOutputs();
            boolean[] tmp = calculateNextState();

            StringBuilder stateBin = new StringBuilder();
            for (int i = 1; i < a.length; ++i) {
                a[i] = tmp[i];
                stateBin.append(tmp[i] ? "1" : "0");
            }

            int state = Integer.parseInt(String.valueOf(stateBin), 2);

            if (state == 0) {
                displayState(state);
                System.out.println("The programme ended!");
                break;
            }

            displayState(state);

            step++;
            if (step == 20) {
                System.out.println("The programme looped!");
                break;
            }
        }
        long endTime = System.currentTimeMillis();
        System.out.printf("Runtime: %d ms\n\n", endTime - startTime);
    }
}
