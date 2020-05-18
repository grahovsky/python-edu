phrase = "Don't panic!"

plist = list(phrase)

print(phrase)
print(plist)

# ranges
# print(plist[0:10:3])
# print(plist[3:])
# print(plist[:10])
# print(plist[::2])
# print(''.join(plist[-6:]))
# print(''.join(plist[::-1]))

for num in range(len(plist)-1, -1, -1):
    if plist[num] not in ["o", "n", " ", "t", "a", "p"]:
        plist.remove(plist[num])
# ont pan

plist.insert(2, plist.pop(3))
# on tpan
plist.insert(4, plist.pop(5))
# on tapn
plist.pop()
# on tap

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)