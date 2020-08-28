def kmpSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix
    # values for pattern

    lps = [0]*M

    computeLPSArray(pat, M, lps)
    i = 0
    j = 0
    while(i < N):
        if(pat[j] == txt[i]):
            j += 1
            i += 1
        if(j == M):
            print(i-j)
            j = lps[j-1]
        elif(i < N and pat[j] != txt[i]):
            if(j != 0):
                j = lps[j-1]
            else:
                i = i + 1


def computeLPSArray(pat, M, lps):
    len = 0
    i = 1
    lps[0]  # lps[0] is always 0
    # the loop calculates lps[i] for i = 1 to M-1
    while(i<M):
        if(pat[i]==pat[len]):
            len+=1
            lps[i] = len;
            i+=1
        else:
            if(len!=0):
                len = lps[len-1]
            else:
                lps[i] = 0
                i+=1

if __name__ == "__main__":
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    kmpSearch(pat,txt)

