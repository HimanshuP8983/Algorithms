package rabinkarp;

public class rabin {
    // d is the number of character in the input alphabet
    public final static int d = 256;

    // pat -> pattern
    // txt -> text
    // q -> a prime number
    static void search(String pat, String txt, int q) {
        int M = pat.length();
        int N = txt.length();
        int i, j;
        int p = 0;// hash value for pattern
        int t = 0; // hash value for text
        int h = 1;

        // The value of h would be "pow(d,M-1)%q"
        for (i = 0; i < M - 1; i++) {
            h = (h * d) % q;
        }

        // Calculate the hash value of pattern and first window of text
        for (i = 0; i < M; i++) {
            p = (d * p + pat.charAt(i)) % q;
            t = (d * t + pat.charAt(i)) % q;
        }

        // Slide the pattern over text one by one
        for (i = 0; i <= N - M; i++) {
            // Check the hash value of current window of text
            // and pattern. If the hash value match then the only
            // check for characters one by one.
            if (p == t) {
                // Check for characters one by one
                for (j = 0; j < M; j++) {
                    if (txt.charAt(i + j) != pat.charAt(j))
                        break;
                }
                if (j == M) {
                    System.out.println(i);
                }
            }

            // Calculate the hash value for next window of text:Remove
            // leading digit, add trailing digit
            if (i < N - M) {
                t = (d * (t - txt.charAt(i) * h) + txt.charAt(i + M)) % q;

                if (t < 0) {
                    t = t + q;
                }
            }
        }
    }

    public static void main(String[] args) {
        String txt = "AABAACAADAABAAABAA";
        String pat = "AABA";
        int q = 101;
        search(pat,txt,q);
    }
}