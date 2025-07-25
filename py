def addsum(n):
    if(n==0):
        return 0
    else:
        return n+ addSum(n-1)
        a= addsum(3)
        print(a)