package finiteautomata;

public class automata {
    public static final int NO_OF_CHARS = 256;

    public static int getNextState(String pat, int M, int state, int x) {
        // If the character c is same as next character
        // in pattern, then simply increment state
        if (state < M && x == pat.charAt(state))
            return state + 1;

        // ns stores the result which is the next state
        int ns, i;
        // ns finally contains the longest prefix
        // which is also suffic in "pat[0..state-1]c"

        // Start from the largest possible value
        // and stop when you find a prefix which is also a suffix
        for (ns = state; ns > 0; ns--) {
            if (pat.charAt(ns - 1) == x) {
                for (i = 0; i < ns - 1; i++) {
                    if (pat.charAt(i) != pat.charAt(state - ns + 1 + i)) {
                        break;
                    }
                    if (i == ns - 1)
                        return ns;
                }
            }
        }
        return 0;
    }

    // This function builds the TF table which represents Finite Automata for a
    // given pattern
    static void computeTF(String pat, int M, int TF[][]) {
        int state, x;
        for (state = 0; state <= M; ++state) {
            for (x = 0; x < NO_OF_CHARS; ++x) {
                TF[state][x] = getNextState(pat, M, state, x);
            }
        }
    }

    // Prints all occurences of pat in text
    static void search(String pat, String txt) {
        int M = pat.length();
        int N = txt.length();
        int[][] TF = new int[M + 1][NO_OF_CHARS];
        computeTF(pat, M, TF);

        //Process txt over FA
        int i,state=0;
        for(i=0;i<N;i++){
            state = TF[state][txt.charAt(i)];
            if(state == M){
                System.out.println(i-M+1);
            }
        }
    }

    public static void main(String[] args){
        String txt = "AABAACAADAABAAABAA";
        String pat = "AABA";
        search(pat,txt);
    }
}