#include<bits/stdc++.h>

void computeLPSArray(char* pat,int M,int* lps);

void KMPSearch(char* pat,char* txt){
    int M = strlen(pat);
    int N = strlen(txt);

    //create lps[] that will hold longest prefix suffix
    // values for pattern
    int lps[M];

    //Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat,M,lps);

    int i=0;//index for text
    int j=0;// index for pat

    while(i<N){
        if(pat[j] == txt[i]){
            j++;
            i++;
        }
        if(j==M){
            printf("%d",i-j);
            j = lps[j-1];
        }else if(i<N && pat[j]!=txt[i]){
            //Do not match lps[0..lps[j-1] characters,
            //they will match
            if(j!=0)
                j = lps[j-1];
            else{
                i = i + 1;
            }
        }
    }
}

//File lps[] for given  pattern pat[0..M-1]
void computeLPSArray(char* pat,int M,int* lps){
    //length of the previous longest prefix suffix
    int len=0;
    lps[0]=0;//lps[0] is always 0
    //the loop calculates lps[i] for i = 1 to M-1
    int i=1;
    while(i<M){
        if(pat[i]==pat[len]){
            len++;
            lps[i] = len;
            i++;
        }else{
            if(len!=0){
                len = lps[len-1];

            }else{
                lps[i]=0;
                i++;
            }
        }
    }
}
int main(){
    char txt[] = "ABABDABACDABABCABAB";
    char pat[] = "ABABCABAB";
    KMPSearch(pat,txt);
    return 0;
}