data = [ 1, 2, 3, 4, 5, 6, 7, 8]
events = []
for num in data:
    if not num % 2:
        events.append(num)

print(events)

events2 = [num for num in data if not num % 2]
print(events2)

data = [ 1, 'one', 2, 'two', 3, 'three', 4, 'four']
words = []
for num in data:
    if isinstance(num, str):
        words.append(num)

print(words)

words2 = [num for num in data if isinstance(num, str)]
print(words2)

data = list('So long and thanks for all the fish'.split())
title = []
for word in data:
    title.append(word.title())

print(title)

title2 = [word.title() for word in data]
print(title2)
