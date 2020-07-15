n = [3,4,5,2,1]

for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        if(n[i]>n[j]):
            temp = n[i]
            n[i] = n[j]
            n[j] = temp

print(n)


# Complexity : 
'''
Worst case : O(n^2)
Best case : omega(n)
Average case : theta(n^2)

# Space Complexity 
Worst case : O(1)
'''