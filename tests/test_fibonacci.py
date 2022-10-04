import pytest
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series
# =========================== fibonacci ================================= 
# n= 0 => 0
# n= 1 or 2 => 1
# n=4 =>3 
# n=5 =>5
# n=6 =>8
# n=-10 =>"Plese enter a positive integer"
# n="s" =>"sorry,Plese enter a positive integer"
def test_fibonacci_one():
    actual= fibonacci(1)
    excepted = 1
    assert actual == excepted
def test_fibonacci_zero():
    actual= fibonacci(0)
    excepted = 0
    assert actual == excepted
def test_fibonacci_four():
    actual= fibonacci(4)
    excepted = 3
    assert actual == excepted
def test_fibonacci_five():
    actual= fibonacci(5)
    excepted = 5
    assert actual == excepted
def test_fibonacci_six():
    actual= fibonacci(6)
    excepted = 8
    assert actual == excepted
def test_fibonacci_minus():
    actual= fibonacci(-10)
    excepted = "Sorry,You entered a negative number"
    assert actual == excepted

def test_fibonacci_str():
    actual= fibonacci("s")
    excepted = "Sorry,You entered a String"
    assert actual == excepted
# =========================== lucas ================================= 
# n= 0 => 2
# n= 1 => 1
# n= 2=> 3
# n= 3=> 4
# n= 7=> 29
# n=-10 =>"Plese enter a positive integer"
# n="s" =>"sorry,Plese enter a positive integer"
def test_lucas_zero():
    actual= lucas(0)
    excepted = 2
    assert actual == excepted
def test_lucas_one():
    actual= lucas(1)
    excepted = 1
    assert actual == excepted
def test_lucas_two():
    actual= lucas(2)
    excepted = 3
    assert actual == excepted
def test_lucas_three():
    actual= lucas(3)
    excepted = 4
    assert actual == excepted 
def test_lucas_seven():
    actual= lucas(7)
    excepted = 29
    assert actual == excepted    
def test_lucas_minus():
    actual= lucas(-10)
    excepted ="Sorry,You entered a negative number"
    assert actual == excepted 
def test_lucas_str():
    actual= lucas("s")
    excepted ="Sorry,You entered a String"
    assert actual == excepted  

# =========================== sum_series =================================

def test_sum_series_f0():
    actual= sum_series(0)
    excepted = 0
    assert actual == excepted
def test_sum_series_f1():
    actual= sum_series(1)
    excepted = 1
    assert actual == excepted
def test_sum_series_f4():
    actual= sum_series(6)
    excepted = 8
    assert actual == excepted 
def test_sum_series_L0():
    actual= sum_series(0, x=2,y=1)
    excepted = 2
    assert actual == excepted  
def test_sum_series_L1():
    actual= sum_series(1, x=2,y=1)
    excepted = 1
    assert actual == excepted
def test_sum_series_L7():
    actual= sum_series(7, x=2,y=1)
    excepted = 29
    assert actual == excepted
def test_sum_series_zero():
    actual= sum_series(0, x=7,y=9)
    excepted = 7
    assert actual == excepted        
def test_sum_series_one():
    actual= sum_series(1, x=7,y=9)
    excepted = 9
    assert actual == excepted 
def test_sum_series_four():
    actual= sum_series(4, x=7,y=9) #7 , 9 , 16, 25,41,66,107,173 
    excepted = 41
    assert actual == excepted
def test_sum_series_seven():
    actual= sum_series(7, x=7,y=9) #7 , 9 , 16, 25,41,66,107,173 
    excepted = 173
    assert actual == excepted 
def test_sum_series_minus():
    actual= sum_series(-10)
    excepted ="Sorry,You entered a negative number"
    assert actual == excepted 
def test_sum_series_str():
    actual= sum_series("s")
    excepted ="Sorry,You entered a String"
    assert actual == excepted 
def test_sum_series_minusY():
    actual= sum_series(1,0,-1)
    excepted ="Sorry,You entered a negative number"
    assert actual == excepted
def test_sum_series_minusX():
    actual= sum_series(1,-1,4)
    excepted ="Sorry,You entered a negative number"
    assert actual == excepted 
def test_sum_series_strX():
    actual= sum_series(1,"x",4)
    excepted ="Sorry,You entered a String"
    assert actual == excepted 
def test_sum_series_strY():
    actual= sum_series(1,3,"y")
    excepted ="Sorry,You entered a String"
    assert actual == excepted 