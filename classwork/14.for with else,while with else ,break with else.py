'''for i in range(1,11):
    if i==12:
        break
    print(i)
else:
    print("end of numbers:")'''





'''for i in range(1,11):
    if i==7:
        break
    print(i)'''    



'''for i in range(1,20,2):
    if i==17:
        break
    print(i)'''


'''for i in range(1,20,2):
    if i==17:
        continue
    print(i)'''




'''for i in range(1,11):
    if i==17:
        continue
    print(i)'''



'''for i in range(1,11):
    if i==7:
        continue
    print(i)'''



'''for i in range(1,100,5):
    print("before print",i)
    if i==11:
        continue
    print(i)'''



#FOR WITH ELSE



'''l=['smartphone','laptop','airpods','shoes']
for i in l:
    print(i.center(20,'_'))
else:
    print('end of the items')'''




'''l=['smartphone','laptop','airpods','shoes']
for i in l:
    if i=='airpods':
        break
    print(i.center(20,'_'))
else:
    print('end of the items')'''



'''bullets=10
while bullets>0:
    print("shoot()")
    bullets-=1
else:
    print("game over")'''



'''bullets=10
while bullets>0:
    if bullets==5:
        print("dead")
        break
    print("shoot()")
    bullets-=1
else:
    print("game over")'''




'''bullets=10
while bullets>0:
    if bullets==15:
        print("dead")
        break
    print("shoot()")
    bullets-=1
else:
    print("game over")'''





bullets=10
while bullets>0:
    if bullets==5:
        print("dead")
        break
    print(f"{bullets} are left-you can shoot()")
    bullets-=1
else:
    print("game over")

























