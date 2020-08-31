def search(pat, txt):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    while(i <= N-M):
        for j in range(M):
            if(txt[i+j] != pat[j]):
                break
            j += 1
        if(j == M):
            print(i)
            i = i + M
        elif(j == 0):
            i = i + 1
        else:
            i = i + j


if __name__ == "__main__":
    txt = "ABCEABCDABCEABCD"
    pat = "ABCD"
    search(pat, txt)
