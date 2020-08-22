def ternarySearch(left,right,key,A):
    if(right>=left):
        mid1 = left + (right-left)//3
        mid2 = right - (right-left)//3
        if(A[mid1]==key):
            return mid1
        if(A[mid2]==key):
            return mid2
        if(key<A[mid1]):
            return ternarySearch(left,mid1-1,key,A)
        elif(key>A[mid2]):
            return ternarySearch(mid2+1,right,key,A)
        else:
            return ternarySearch(mid1+1,mid2-1,key,A)
    return None

if __name__ == "__main__":
    N,key = map(int,input().split(" "))
    A = [int(N) for N in input().split(" ")]
    A.sort()
    print("Sorted List: ",A)
    left = 0
    right = len(A)-1
    idx = ternarySearch(left,right,key,A)
    print("Element found at index: ",idx)