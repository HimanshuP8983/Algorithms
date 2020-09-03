package boyermoore;

public class boyermoore {
    public static final int NO_OF_CHARS = 256;

    public static int max(int a, int b) {
        return (a > b) ? a : b;
    }

    public static void badCharHeuristic(char[] str, int size, int badchar[]) {
        int i;

        // Initialize all occurences as -1
        for (i = 0; i < NO_OF_CHARS; i++) {
            badchar[i] = -1;
        }

        // Fill the actual value of last occurences of a character
        for (i = 0; i < size; i++) {
            badchar[(int) str[i]] = i;
        }
    }

    // A pattern searching function that uses Bad Character Heuristic of Bouer Moore
    // Algorithm
    public static void search(char txt[], char pat[]) {
        int m = pat.length;
        int n = txt.length;
        int[] badchar = new int[NO_OF_CHARS];

        /*
         * Fill the bad character array by calling the preprocessing function
         * badCharHeuristic for given pattern
         */
        badCharHeuristic(pat, m, badchar);

        int s = 0; // s is shift of the pattern respect to text
        while (s <= (n - m)) {
            int j = m - 1;
            /*
             * keep reducing index j of pattern while characters of pattern and text
             * arematching at this shift s
             */
            while (j >= 0 && pat[j] == txt[s + j])
                j--;

            /*
             * If the pattern is present at current shift, then index j will become -1 after
             * the aboove loop
             */
            if (j < 0) {
                System.out.println(s);
                s += (s + m < n) ? m - badchar[txt[s + m]] : 1;
            } else {
                s += max(1, j - badchar[txt[s + j]]);
            }
        }
    }

    public static void main(String[] args) {
        char txt[] = "ABAAABCD".toCharArray();
        char pat[] = "ABC".toCharArray();
        search(txt, pat);
    }
}
