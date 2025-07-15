Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> t=()
>>> t=tuple=()
>>> t=(1,2,3,4,"strings")
>>> t
(1, 2, 3, 4, 'strings')
>>> t[:5]
(1, 2, 3, 4, 'strings')
>>> t[:4]
(1, 2, 3, 4)
>>> t
(1, 2, 3, 4, 'strings')
>>> t2=('python','list','tuple')
>>> t+t2
(1, 2, 3, 4, 'strings', 'python', 'list', 'tuple')
>>> t[:4]*3
(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
>>> 4 int
SyntaxError: invalid syntax
>>> 4 in t
True
>>> 5 in t
False
>>> t=(1,2,3)
>>> a,b,c=t
>>> a
1
>>> 2
2
>>> 
>>> b
2
>>> c
3
>>> res=('arun','arun@gmail','arun@123')
>>> name,gmail,pwd=res
>>> name
'arun'
>>> amail
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    amail
NameError: name 'amail' is not defined
>>> gmail
'arun@gmail'
>>> pwd
'arun@123'
>>> res
('arun', 'arun@gmail', 'arun@123')
>>> t=('1,2,3,4,1,2,3,4,7,,5,3,4,7,8,9)
       
SyntaxError: EOL while scanning string literal
>>> t=('1,2,3,4,1,2,3,4,7,,5,3,4,7,8,9')
       
>>> t.count(1)
       
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    t.count(1)
TypeError: must be str, not int
>>> t=('1,2,3,4,5,6,7,8,9,3,4,5,6,7,8,9,1,')
       
>>> t.count(2)
       
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    t.count(2)
TypeError: must be str, not int
>>> t=('1,2,3,4,5,6,7,8,9,3,4,5,6,7,8,9,1')
       
>>> t.count(1)
       
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    t.count(1)
TypeError: must be str, not int
>>> 
       

>>> 
       
>>> 
       
>>> 
       
>>> 
       
>>> 
       
>>> 
