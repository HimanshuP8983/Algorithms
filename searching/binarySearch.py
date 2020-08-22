def binarySearch(A,key):
    key = int(key)
    low = 0
    high = len(A)-1
    while(low<=high):
        mid = (high + low) // 2
        if(A[mid]<key):
            low = mid + 1
        elif(A[mid]>key):
            high = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    N, key = input().split(" ")
    A = [int(N) for N in input().split(" ")]
    A.sort()
    print(A)
    idx = binarySearch(A,key)
    print(idx)

'''
A = [4,2,1,6,5]
    low  mid  high(A.length-1)
Algo:
1. A.sort()
2. A = [1,2,4,5,6]
3. binarySearch(A,key=2)
4. low=0, high=len(A), mid=len(A)//2
5. while(low<=high):
6.  if(A[mid]<key):         #A[mid] = 4 < 5
7.      low = mid + 1      #low = 3       
8.  elif(A[mid]>key):        #A[mid] = 4 > 2
9.      high = mid - 1
10. else:
11.     return mid
'''


'''
def tanuja():
    var = 1         # Local Scope

def xyz():
    print(var)

if __name__=="__main__":
    var = 2
    tanuja()
    xyz()
'''