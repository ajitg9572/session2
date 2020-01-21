ammount =int(input("enter ammount"))
user_input =input("Do you want to ganerate key 'yes' and 'no'")
shift = ammount >>8
if ammount >=100000 and user_input=="yes":
    print("your coded ammount key is:",shift)
else:
    print("your amount",ammount)