Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name=input("enter the name:")
enter the name:python
>>> name
'python'
>>> type(name)
<class 'str'>
>>> age=int("enter the age:")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    age=int("enter the age:")
ValueError: invalid literal for int() with base 10: 'enter the age:'
>>> age=input("enter the age:")
enter the age:70
>>> age
'70'
>>> type(age)
<class 'str'>
>>> age=int(input("enter the age:"))
enter the age:70
>>> age
70
>>> type(age)
<class 'int'>
>>> discount=float(input("enter the discount:"))
enter the discount:45.5
>>> discount
45.5
>>> type(discount)
<class 'float'>
>>> names=input("enter the names:")
enter the names:ramya rajeswari sandhya
>>> names
'ramya rajeswari sandhya'
>>> names=input("enter the names:").split()
enter the names:ramya rajeswari sandhya
>>> names
['ramya', 'rajeswari', 'sandhya']
>>> num=input("enter numbers:").split()
enter numbers:1234
>>> num
['1234']
>>> num=int(input("enter the numbers:").split())
enter the numbers: 4 5 6 7 8
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    num=int(input("enter the numbers:").split())
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> num=map(int,input("enter the numbers:").split())
enter the numbers:1 2 3 4 5 
>>> num
<map object at 0x000001D24EEBDF28>
>>> num=list(map(int,input("enter the numbers:").split()))
enter the numbers:1 2 3 4 5 
>>> num
[1, 2, 3, 4, 5]
>>> num=list(map(float,input("enter the numbers:").split()))
enter the numbers:12.3 12 14.5 34 56 45.7
>>> num
[12.3, 12.0, 14.5, 34.0, 56.0, 45.7]
>>> um=list(map(input("enter the numbers:").split()))
enter the numbers:123 123 345
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    um=list(map(input("enter the numbers:").split()))
TypeError: map() must have at least two arguments.
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> num=set(input("enter numbers:").split())
enter numbers: dsdkfaj dksajf dskaf lkj
>>> num
{'lkj', 'dsdkfaj', 'dksajf', 'dskaf'}
>>> num=eval(input("enter the dict:"))
enter the dict:{'name':'xyz','age':89}
>>> num
{'name': 'xyz', 'age': 89}
>>> n=bool(input("enter the status:"))
enter the status:True
>>> n
True
>>> name,email,pwd=input("enter the data:").split()
enter the data:arun arun@gmail.com arun@123
>>> name
'arun'
>>> email
'arun@gmail.com'
>>> pwd
'arun@123'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a,b,c=12,23.4,'string'
>>> a
12
>>> b
23.4
>>> c
'string'
>>> print(a,b,c)
12 23.4 string
>>> print("a:",a,'b:',b,'c:',c)
a: 12 b: 23.4 c: string
>>> print('%d,%f,%s'%(a,b,c))
12,23.400000,string
>>> print('a: %d b: %f c: %s'(a,b,c))
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print('a: %d b: %f c: %s'(a,b,c))
TypeError: 'str' object is not callable
>>> print('a: %d b: %f c: %s'%(a,b,c))
a: 12 b: 23.400000 c: string
>>> print(f'{a}{b}{c}')
1223.4string
>>> p
