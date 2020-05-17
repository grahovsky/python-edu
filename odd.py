from datetime import datetime
import time, random

odds = [ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

for i in range(5):

    print(time.strftime("%I:%M:%S"))

    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("This minute seems a little odd")
    else:
        print("Not an odd minute.")

    if i < 4:
        
        timeToSleep = random.randint(15,30)

        print("Sleep {timeToSleep}".format(timeToSleep = timeToSleep))
        time.sleep(timeToSleep)
