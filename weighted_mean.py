def weighted_mean(arr):
    n = len(arr)
    #print(n)
    a1 = 2/(n*(n+1))
    #print(a1)
    d = 2*(1-n*a1)/(n*(n-1))
    #print(d)
    x = 0
    for i in range(1,n+1):
        x = x + (arr[i-1]*(a1))
        a1 = a1 + d
        
    return x
