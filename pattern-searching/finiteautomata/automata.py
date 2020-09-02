NO_OF_CHARS = 256


def getNextState(pat, M, state, x):
    if(state < M and x == ord(pat[state])):
        return state + 1

    ns = 0
    i = 0
    for ns in range(state, ns, ns - 1):
        if(pat[ns-1] == x):
            for i in range(0, ns-1):
                if(pat[i] != pat[state - ns + 1 + i]):
                    break
            if(i == ns-1):
                return ns
    return 0        


def computeTF(pat, M):
    global NO_OF_CHARS
    TF = [[0 for i in range(NO_OF_CHARS)]
          for _ in range(M+1)]

    for state in range(M+1):
        for x in range(NO_OF_CHARS):
            z = getNextState(pat, M, state, x)
            TF[state][x] = z

    return TF


def search(pat, txt):
    global NO_OF_CHARS
    M = len(pat)
    N = len(txt)
    TF = computeTF(pat, M)

    # Process txt over FA
    state = 0
    for i in range(N):
        state = TF[state][ord(txt[i])]
        if(state == M):
            print(format(i-M+1))


if __name__ == "__main__":
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(pat, txt)
