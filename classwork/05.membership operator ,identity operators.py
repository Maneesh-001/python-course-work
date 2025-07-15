#5.Membership operator

names=['sumanth','tarak','sanjay','charan','vaishyanci']
print('in result:','rahul'in names) #in result: False
print('not in result:','suhas' not in names) #not in result: True


#6.Identity operators
>>> l=[1,2,3,4]
>>> b=[1,2,3,4]
print("l is b:",l is b)#l is b False
a=b #assign b to a
print("a is b:",a is b)
print("id(l)",id(l))#id(l)1989444535112
print("id(b)",id(b))#id(b)1989444535432
print("id(a)",id(a))#id(a)1989444535432
print("a is not b:",a is not b)
print("l is not b:",l is not b)
>>> l==b
True
>>> 
>>> a=b
>>> a is b
True
>>> 
>>> 
>>> 
>>> a is not b
False
>>> l is not b
True
>>> 

'''1-001
2-010
3-011
4--100
5-101
6-110
------
3&5=001=1'''
print("3&5: ",3&5)

'''4-100
5-101
-------
4|5=101=5'''
print("4|5: ",4|5)

'''5-101
6-110
-------
5^6=011=3'''
print("5^6: ",5^6)

'''1-001
-----
~1=100'''
print("~1:,",~1)

'''2<<1
2=010
4=100'''
print("2<<1: ",2<<1)
'''4>>1
4=100
2=010'''
print("4>>1: ",4>>1)
