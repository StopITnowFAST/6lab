word = 'heheheha'
counter = 0

for i in range(len(word)):
    if word[i] in word[i+1:len(word)]:
        counter += 1

print(len(word)-(counter))
