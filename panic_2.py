phrase = "Don't panic!"

plist = list(phrase)

print(phrase)
print(plist)

plist = plist[1:8]

templist = plist.copy()
templist = templist[1:8]

plist = plist[0:2]
plist.extend(templist[3:1:-1])
plist.extend(templist[-1:-3:-1])

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)