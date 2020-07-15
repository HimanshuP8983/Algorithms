def heapify(arr,n,i):
    # Find the largest element among the root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l<n and arr[i]<arr[l]:
        largest = l
    
    if r<n and arr[largest]<arr[r]:
        largest = r
    
    if largest!=i:
        arr[i],arr[largest] = arr[largest], arr[i]
        heapify(arr,n,largest)

def heapSort(arr):
    n = len(arr)

    # Build max heap 
    for i in range(n//2, -1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        #Swap 
        arr[i],arr[0] = arr[0],arr[i]

        #heapify root element
        heapify(arr,i,0)

if __name__ == "__main__":
    A = [int(N) for N in input().split(" ")]
    heapSort(A)
    print("Sorted: ",A)
