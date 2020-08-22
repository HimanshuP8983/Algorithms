def countingSort(A):
    size = len(A)
    #Step 1:
    max_val = max(A)
    #Step 2:
    count = [0]*(max_val+1)
    #Step 3:
    for i in range(0,size):
        count[A[i]] += 1
    #print(count)
    #Step 4: Cumulative Sum 
    for i in range(1,len(count)):
        count[i] += count[i-1]
    #print(count)
    output = [0]*size
    i = size-1
    while(i>=0):
        output[count[A[i]]-1]=A[i]
        count[A[i]]-=1
        i-=1
    
    print("Sorted List: ",output)
    
if __name__ == "__main__":
    N = int(input())
    A = [int(N) for N in input().split(" ")]
    countingSort(A)