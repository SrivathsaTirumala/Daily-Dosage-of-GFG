def pos(n):
    for i in range(n-1,-1,-1):
        print(i, end=" ")
        
    
def neg(n):
    i=n
    while i<=0:
        print(i, end=" ")
        i+=1
        
    
def result(n):
    if n==0:
        print("already Zero")
    elif n>0:
        pos(n)
    else:
        neg(n)