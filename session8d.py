solutation ="Mr."
fname ="Gourge"
full_name=solutation+fname
print(full_name)
print("solutation",solutation)

number ="110"
print("number is",number,type(number))

print("is digit",number.isdigit())

song_name =input("enter song name")
if song_name.endswith(".mp3"):
    print("you can play the music")
else:
    print("audio file not supported")