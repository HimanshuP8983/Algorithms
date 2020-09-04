NO_OF_CHARS = 256


def badCharHeuristic(str, size):
    global NO_OF_CHARS
    i = 0

    # Initialize all occurences as -1
    badchar = [-1]*NO_OF_CHARS

    # fill the actual value of last occurences of a character
    for i in range(0, size):
        badchar[ord(str[i])] = i

    return badchar


def search(txt, pat):
    global NO_OF_CHARS
    m = len(pat)
    n = len(txt)

    # Fill the bad characters by calling the preprocessing function
    # badCharHeuristic for gien pattern
    badchar = badCharHeuristic(pat, m)
    s = 0
    while(s <= (n-m)):
        j = m-1
        # keep reducing index j of pattern while characters of pattern and text
        # are matching at this shift s
        while(j >= 0 and pat[j] == txt[s+j]):
            j -= 1

        # If the pattern is present at current shift, then index j will become -1 after the above loop
        if(j < 0):
            print(s)
            s += (m - badchar[ord(txt[s+m])] if s+m<n else 1)
        else:
            s += max(1, j-badchar[ord(txt[s+j])])

if __name__ == "__main__":
    txt="ABAAABCD"
    pat="ABC"
    search(txt, pat)
