def exponent(b,n):
    if(n==0):
        return 1
    elif(n%2==1):
        return b*exponent(b,n-1)
    else:
        return exponent(b,n/2)**2

ans = exponent(10,10247)
print("Ans: ",ans)