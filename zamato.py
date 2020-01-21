ammount =float(input("enter ammount"))
coupon = input("applied coupon")
discount =ammount - (0.4*ammount)
jumbo = ammount -150
if discount < 100 and coupon =="zamato":
    print("40% off coupon is appliied ,your effective price is \u20b9",discount) 
elif  discount >100 and coupon=="zamato":
    ammount -=100
    print("40% off coupon is appliied upto 100,your effective price is \u20b9",ammount)
elif ammount>=500 and coupon=="jumbo":
    print("congratulation! 50 % off,your effective price is \u20b9",jumbo)
else:
    print("you are not applied any coupon your effective  price is \u20b9",ammount)
    print("availible coupon is 'zamato'to 40 % off and 'jumbo' off 50% upto 150") 

    

