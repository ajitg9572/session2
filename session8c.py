def split(sentences):
    words =[]

    if " " in sentences:
        sentences.replace(" ","+")
        words.append(sentences)
word ="Search the Candle, rather than cursing the darkness"
print(split(word))