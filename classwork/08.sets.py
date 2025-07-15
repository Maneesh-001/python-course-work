Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s=set()
>>> s={1,2,3,4,3,5,6}
>>> s
{1, 2, 3, 4, 5, 6}
>>> class={'arun','gopal','sumanth','nimisha','shivani','smitha'}
SyntaxError: invalid syntax
>>> class30={'arun','gopal','sumanth','nimisha','shivani','smitha'}
>>> class30
{'arun', 'smitha', 'shivani', 'nimisha', 'sumanth', 'gopal'}
>>> 'arun' in class30
True
>>> 'suhas' not in class30
True
>>> girls={'darshitha','sushmitha','ramya','sandya'}
>>> boys={'arun','sanjay','gopi','maneesh'}
>>> girls | boys
{'sushmitha', 'arun', 'darshitha', 'gopi', 'sandya', 'maneesh', 'sanjay', 'ramya'}
>>> girls & boys
set()
>>> class30 & boys
{'arun'}
>>> class30-boys
{'smitha', 'shivani', 'nimisha', 'sumanth', 'gopal'}
>>> class30 ^ boys
{'gopi', 'smitha', 'maneesh', 'sanjay', 'shivani', 'nimisha', 'sumanth', 'gopal'}
>>> a={1,2,3,4,5,}
>>> a
{1, 2, 3, 4, 5}
>>> b={3,4}
>>> a<=b
False
>>> b>=a
False
>>> a>=b
True
>>> girls.isdisjoint(boys)
True
>>> boys
{'sanjay', 'maneesh', 'gopi', 'arun'}
>>> boys.add('sumanth')
>>> boys
{'arun', 'gopi', 'maneesh', 'sanjay', 'sumanth'}
>>> boys.remove('gopi')
>>> boys
{'arun', 'maneesh', 'sanjay', 'sumanth'}
>>> boys.pop
<built-in method pop of set object at 0x0000017FD4D59E48>
>>> boys.pop()
'arun'
>>> girls
{'darshitha', 'sandya', 'ramya', 'sushmitha'}
>>> girls.update({'vaishnavi','hema','nikitha','sravani'})
>>> girls
{'sushmitha', 'sravani', 'darshitha', 'sandya', 'vaishnavi', 'hema', 'nikitha', 'ramya'}
>>> a={1,2,3,4,5}
>>> b={3,4,5,6,7,}
>>> a | b
{1, 2, 3, 4, 5, 6, 7}
>>> a
{1, 2, 3, 4, 5}
>>> b
{3, 4, 5, 6, 7}
>>> a & b
{3, 4, 5}
>>> a.intersection_update(b)
>>> a
{3, 4, 5}
>>> b
{3, 4, 5, 6, 7}
>>> c.a.copy()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    c.a.copy()
NameError: name 'c' is not defined
>>> c=a.copy()
>>> c.add(7)
>>> c
{3, 4, 5, 7}
>>> c.add(8)
>>> c
{3, 4, 5, 7, 8}
>>> girls
{'sushmitha', 'sravani', 'darshitha', 'sandya', 'vaishnavi', 'hema', 'nikitha', 'ramya'}
>>> len(girls)
8
>>> max(girls)
'vaishnavi'
>>> f=frozenset({1,2,3,4,})
>>> f
frozenset({1, 2, 3, 4})
>>> type(f)
<class 'frozenset'>
>>> len(f)
4
>>> 
