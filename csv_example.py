from datetime import datetime
import pprint

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint.pprint(flights)
print
flights2 = {}

for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()


pprint.pprint(flights2)

# example comprehensions
# list
more_dests = [dest.title() for dest in flights.values()]
pprint.pprint(more_dests)

# dict
more_flights = {convert2ampm(k): v.title() for k, v in flights.items() if v == 'FREEPORT'}
pprint.pprint(more_flights)

when = {}
for dest in set(flights.values()):
    when[dest] = [k for k, v in flights.items() if v == dest]
pprint.pprint(when)

when2 = {dest: [k for k, v in flights.items() if v == dest] for dest in set(flights.values())}
pprint.pprint(when2)
