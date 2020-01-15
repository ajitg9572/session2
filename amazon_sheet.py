amazon_price =int(input("enter ammout of sale"))
profit_margin =int(input("enter profit margin"))
tax =int(input("tax in percentage"))
day1=int(input("day1 sale"))
day2 =int(input("day 2 sale"))
day3=int(input("day 3 sale"))
total_sallng =day1+day2+day3
total_profit =profit_margin*total_sallng
taxpaytogov=(total_profit)//100*(tax)
print("total selling",total_sallng)
print("total profit",total_profit)
print("tax pay",taxpaytogov)