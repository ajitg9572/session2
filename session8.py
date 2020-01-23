name = "Fionna Flynn"
print(">> name is ",name)
new_name=name.upper()
print(">> name now ",new_name)


author_name="john watson"
author_name=author_name.capitalize()
print(author_name)


quotes = "Work Hard,Get Luckier Search the Candle,rather thaan cursing the darkness""
def count(data, word, start, end):
c=0
j=0
for i in range(start,end):
    print(data[i]==word[j])
    j+=1
    i+=j
return c
print(">> the occur",count(quotes,"the",0,len(quotes)))