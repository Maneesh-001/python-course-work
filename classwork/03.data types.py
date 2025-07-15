Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: C:/Users/saima/OneDrive/Desktop/dataype.py ============
Traceback (most recent call last):
  File "C:/Users/saima/OneDrive/Desktop/dataype.py", line 2, in <module>
    type(a)
NameError: name 'a' is not defined
>>> 
============ RESTART: C:/Users/saima/OneDrive/Desktop/dataype.py ============
>>> 
=========== RESTART: C:/Users/saima/OneDrive/Desktop/int values.py ===========
>>> int_a=12
int_c=0
int_b=-12
type(int_c)
SyntaxError: multiple statements found while compiling a single statement
>>> 
int_a=12
int_c=0
int_b=-12
type(int_c)
SyntaxError: multiple statements found while compiling a single statement
>>> int_a=12
>>> int_b=23
>>> int_c=20
>>> type(int_c)
<class 'int'>
>>> d={}
>>> type(d)
<class 'dict'>
>>> t={1,2,3,4)
SyntaxError: invalid syntax
>>> type(t)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    type(t)
NameError: name 't' is not defined
>>> t=(1,2,3,4,5)
>>> type(t)
<class 'tuple'>
>>> t
(1, 2, 3, 4, 5)
>>> t=(1,2,3,'string',true)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t=(1,2,3,'string',true)
NameError: name 'true' is not defined
>>> t=(1,"string")
>>> t
(1, 'string')
>>> t=(1,'string',3.41,false)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    t=(1,'string',3.41,false)
NameError: name 'false' is not defined
>>> d={'name'='gopi','course':'python'}
SyntaxError: invalid syntax
>>> d={'name':'gopi','course':'python'}
>>> d
{'name': 'gopi', 'course': 'python'}
>>> s=False
>>> type(s)
<class 'bool'>
>>> t=(1,'string',3.14,False)
>>> t
(1, 'string', 3.14, False)
>>> 
