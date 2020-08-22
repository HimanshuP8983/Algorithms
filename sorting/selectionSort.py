n = [3,2,1,4,5]

for i in range(0,len(n)):           #Assumed to have smallest value
    pos = i                     
    for j in range(i+1,len(n)):
        if(n[pos]>n[j]):
            pos = j
    temp = n[i]
    n[i] = n[pos]
    n[pos] = temp

print(n)

'''
Complexity:

Time Complexity
1. worst case : O(n^2)
2. average case : theta(n^2)
3. best case : omega(n)

Space Complexity
worst case : O(1) 
'''