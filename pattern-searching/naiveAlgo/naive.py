def search(pat,txt):
    M = len(pat)
    N = len(txt)
    for i in range(0,N-M+1):
        j=0
        while(j<M):
            if(txt[i+j]!=pat[j]):
                break
            j+=1
        if(j==M):
            print(i)

if __name__ == "__main__":
    txt = 'AABAACAADAABAAABAA'
    pat = 'AABA'
    search(pat,txt)