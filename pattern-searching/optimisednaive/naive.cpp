#include <bits/stdc++.h>
using namespace std;

void search(string pat, string txt)
{
    int M = pat.size();
    int N = txt.size();
    int i = 0;
    while (i <= N - M)
    {
        int j;
        //for current index i, check for pattern match
        for (j = 0; j < M; j++)
        {
            if (txt[i + j] != pat[j])
                break;
        }
        if (j == M)
        {
            cout << i << endl;
            i = i + M;
        }else if(j==0){
            i = i + 1;
        }else{
            i = i + j;
        }
    }
}
int main(){
    string txt="AABAACAADAABAAABAA";
    string pat = "AABA";
    search(pat,txt);
    return 0;
}