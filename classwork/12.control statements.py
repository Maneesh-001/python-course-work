'''name='arun'
for ch in name:
    print(f"ch = {ch}")'''


'''name=('dinesh','gopal','shivani','prashanth')
for ch in name:
    print(f"ch = {ch}")'''


'''name={'dinesh','gopal','shivani','prashanth'}
for ch in name:
    print(f"ch = {ch}")'''


'''name={1:'dinesh',2:'gopal',3:'shivani',4:'prashanth'}
for i in name.keys():
    print(f'{i}-{name[i]}')'''



'''name={1:'dinesh',2:'gopal',3:'shivani',4:'prashanth'}
for i in name.keys():
    print(f'{i}-{name[i].titile()}')'''


# range

'''for i in range(0,10):
    print(i)'''



'''for i in range(2,21,2):
    print(i)'''
               

'''for i in rage(20,1,-2):
    print(i)'''



'''for i in range(1,21):
    print(f'2 * {1} = {2*i}')'''


'''for i in range(1,21):
    print(f'17 * {1} = {17*i}')'''


'''a=1
while a<=10:
    print(a)
    a+=1'''

#login attempt

email,pwd='xyz@gmail.com','xyz@123'

max_attempt=5
cur_attempt=1

while cur_attempt <=max_attempt:
    e=input("enter the email:")
    p=input("enter the password:")
    if e==email and p==pwd:
        print("login successful")
    else:
        print("invalid email or pwd.try again!!")
    cur_attempt+=1
else:
    print("max attempts are done.try after 5min")



