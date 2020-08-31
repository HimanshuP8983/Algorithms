package optimisednaive;

public class naive {
    public static void search(String pat, String txt) {
        int M = pat.length();
        int N = txt.length();
        int i = 0;
        while (i < N - M) {
            int j;
            // for current index i, check for pattern search
            for (j = 0; j < M; j++) {
                if(txt.charAt(i+j)!=pat.charAt(j))
                    break;
            }
            if(j==M){
                System.out.println(i);
                i = i + M;
            }else if(j==0){
                i = i + 1;
            }else{
                i = i + j;
            }
        }
    }

    public static void main(String[] args){
        String pat = "AABAACAADAABAAABAA";
        String txt = "AABA";
        search(pat,txt);
    }
}