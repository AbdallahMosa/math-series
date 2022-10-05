def fibonacci(n):
    if type(n)!=int:
       return "Sorry,You entered a String"
    if n < 0:
       return "Sorry,You entered a negative number"
    if n ==0:
        return 0
    if n == 1 or n ==2:
        return 1
    else :
        return(fibonacci(n-1) + fibonacci(n-2))

def lucas(n):
    if type(n)!=int:
       return "Sorry,You entered a String"
    if n < 0:
       return "Sorry,You entered a negative number"
    if n ==0:
        return 2
    if n == 1 :
        return 1
    else :
        return lucas(n - 1) + lucas(n - 2)

# sum_series
def sum_series(n,x=0 ,y=1):
    if type(n)!=int or type(x)!=int  or type(y)!=int:
       return "Sorry,You entered a String"
    if n < 0 or x < 0 or y< 0:
       return "Sorry,You entered a negative number"
    if x==0 and y ==1:
         return fibonacci(n)
    if x==2 and y ==1:
        return lucas(n)
    if n==0:
        return x 
    if n ==1 :
        return y
    else :
        return sum_series(n-1,x=x,y=y)+sum_series(n-2,x=x,y=y)

