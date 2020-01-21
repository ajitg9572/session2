username =input("enter your username")
password =input('enter password')
kilometer =int(input('enter ride distance (km)'))
wallet =int(input("enter wallet ammount"))
price =kilometer*10
if username=="ajit1234" and password=="ajit1234":
    print("welcome! Login Successful")
else:
    print("Login Failed")    
if wallet>= price and username=="ajit1234" and password=="ajit1234":
    print("Successful book a car")
    otp=int(input("enter otp to conform booking"))
    print(otp==1234)
else:
    print("Booking Failed")


