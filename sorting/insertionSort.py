n = [3,2,1,4,5]

for j in range(1,len(n)):
    key = n[j]
    i = j-1
    while(i>=0 and n[i]>key):
        n[i+1] = n[i]
        i = i - 1
    n[i+1] = key

print(n)

'''
Space Complexity:

Worst case: O(1) 
'''