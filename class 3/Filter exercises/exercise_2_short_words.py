words = ["learn", "code", "AI", "math"]

short_words = list(filter(lambda x:len(x) < 5, words))

print(short_words)