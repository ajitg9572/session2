name="John watson"
print(name,type(name),hex(id(name)))

print("lenght of name",len(name))
print("minimum of name",min(name))
print("maximum of name",max(name))

print(name[1])
print(name[len(name)-1])


print(name[0:4])
print(name[1],name[-2])

print(name[::-1])

phone =input("enter your phone number")
email =input("enter your email")
if "@" in email  and "." in email :
    print("valid mail")
else:
    print("invalid email")

if len(phone) >10 and len(phone) <=15:
     print("valid phone number")
else:
     print("invalid phone number")