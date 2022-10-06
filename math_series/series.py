def fibonacci(n):
    """
       fibonacci series where each number is the sum of the two that precede it. It starts from 0 and 1 usually. The  sequence is given by 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on
    """
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

    """
    lucas series where each number is the sum of the two that precede it. It starts from 2 and 1 usually
     ex : 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123

    """
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
    """
     this function sum_series where each number is the sum of the two that precede it. if  starts from 0 and 1 can we call it, if  starts from 2 and 1 can we call it lucas  Otherwise you can starts with any number you want 
    

    """
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

