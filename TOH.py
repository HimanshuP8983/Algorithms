#Tower of Hanoi
def TOH(n,A,B,C):
    if(n>0):
        TOH(n-1,A,C,B)
        print("Move a disc from {} to {}",A,C)
        TOH(n-1,B,C,A)

if __name__ == "__main__":
    n = int(input())
    TOH(n,1,2,3)