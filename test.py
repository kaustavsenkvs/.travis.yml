from calculator import add
from calculator import subtraction
from calculator import multiplication
from calculator import division

def test_add():
  assert add(2,6)==8

def test_wrong_add():
  assert add(2,6)==7

def test_subtract():
  assert subtraction(2,6)==-4
  
def test_multiply():
  assert multiplication(2,9)==18
  
def test_divide():
  assert division(3,1)==1
