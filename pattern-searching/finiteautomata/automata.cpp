#include <bits/stdc++.h>
using namespace std;
#define NO_OF_CHARS 256

int getNextState(string pat, int M, int state, int x)
{
    //if the character c is same as next character
    // in pattern, then simply increment state
    if (state < M && x == pat[state])
        return state + 1;

    //ns stores the result which is the next state
    int ns, i;
    //ns finally contains the longest prefix
    //which is also suffix in "pat[0..state-1]c"

    //Start from the largest possible value
    //and stop when you find a prefix which is also a suffix
    for (ns = state; ns > 0; ns--)
    {
        if (pat[ns - 1] == x)
        {
            for (i = 0; i < ns - 1; i++)
            {
                if (pat[i] != pat[state - ns + 1 + i])
                {
                    break;
                }
            if (i == ns - 1)
                return ns;
            }
        }
    }
    return 0;
}

void computeTF(string pat, int M,int TF[][NO_OF_CHARS])
{
    int state, x;
    for(state=0;state<=M;++state){
        for(x=0;x<NO_OF_CHARS;++x){
            TF[state][x] = getNextState(pat,M,state,x);
        }
    }
}

//Prints all occurences of pat in text
void search(string pat, string txt){
    int M = pat.size();
    int N = txt.size();
    int TF[M+1][NO_OF_CHARS];
    computeTF(pat,M,TF);

    //Process txt over FA.
    int i, state=0;
    for(i=0;i<N;i++){
        state = TF[state][txt[i]];
        if(state == M){
            cout<< i-M+1<<"\n";
        }
    }
} 
int main(){
    string txt = "AABAACAADAABAAABAA";
    string pat = "AABA";
    search(pat,txt);
    return 0; 
}