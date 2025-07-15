'''data={
'prashanth@gmail.com':'123@',
'dinesh@gmail.com':'456!',
'sanjay@gmail.com':'234',
}
email,pwd=input("enter the eamil and pwd: ").split()
if data.get(email)== pwd:
    print('login successful')
else:
    print('invalid login')'''

'''items=['coffee','icecream','samosa','idly']
stocks=[20,50,40,0]
data=input("enter the item:")


if data in items:
    ind=items.index(data)
    if stocks[ind]>0:
        print("available")
    else:
        print('out of stock.please try again')
    
else:
    print('item not available')'''

items=['coffee','icecream','samosa','idly']
stocks=[20,50,40,0]
distance=[13,4,5,9,12]
ratings=[3.2,4,4,3.1,]
cost=[150,60,20,40]
veg=[True,True,False,True]

data=input("enter the item: ")
ind=items.index(data)

if distance[ind]<5 and rating[ind]>4 and cost[ind]<500 and veg[ind] and time[ind]
    print('time,veg,cost,distance and rating applied')
elif distance[ind]<5 and rating[ind]>4 and cost[ind]<500 and veg[ind]:
    print('veg,cost,distance and rating applied')
elif distance[ind]<5 and rating[ind]>4 and cost[ind]<500:
    print('cost,distance and rating applied')
elif istance[ind]<5 and rating[ind]>4 and cost[ind]<500:
    print('cost')
else:
    print('show all products')
          
