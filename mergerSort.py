'''
# I/P:
n = [1,5,6,2,4,7]

l = [1,5,6] # pointer i, i+1+1 # n/2
r = [2,4,7] # pointer j, j+1+1 # n/2

# O/P:
nlist = [1,2,4,5,6,7]
         p     q   r

# Complexity :
# worst case = O(nlogn).

The list of size N is divided into max of logN parts, and the merging of all sublists into a single list takes O(N) time, the worst case run time of this algorithm is O(NlogN)
'''

def mergeSort(nlist):
    if(len(nlist)>1):
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        print('Lefthalf: ',lefthalf)
        righthalf = nlist[mid:]
        print('Righthalf: ',righthalf)

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=j=k=0
        
        while(i<len(lefthalf) and j<len(righthalf)):
            if(lefthalf[i]<righthalf[j]):
                nlist[k] = lefthalf[i]
                i+=1
            else:
                nlist[k] = righthalf[j]
                j+=1
            k+=1
        
        while(i<len(lefthalf)):
            nlist[k] = lefthalf[i]
            i+=1
            k+=1
        
        while(j<len(righthalf)):
            nlist[k] = righthalf[j]
            j+=1
            k+=1

if __name__=="__main__":
    n = int(input())
    nlist = [int(n) for n in input().split()]
    mergeSort(nlist)
    print("MergeSort: ",nlist)


# artificial busyness
