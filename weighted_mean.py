def weighted_mean(arr):
    n = len(arr)
    #print(n)
    a1 = 2/(n*(n+1))
    x = 0
    for i in range(1,n+1):
        x = x + (i*arr[i-1])
        
    x = a1*x
    return x
