# HEALTHY PROGRAMMER APP BY ROBIN SINGH KUNTAL

# Reminder for you to Drink 3.5 ltrs of water everyday

# Reminder for you to give your eyes every 30 min

# Reminder for you to do physical activity every 45 min while working

import time
from datetime import datetime
from pygame import mixer

mixer.init()
mixer.music.set_volume(0.7)

print("\t\t\t\t\t\t Welcome To Healthy Programmer Application")

start_time = str("9:00:00")
end_time = str("17:00:00")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
water_goal = 0

while water_goal <=3500:
    if current_time < end_time or current_time > start_time:
        while True:
            time.sleep(3)
            mixer.music.load("Water.mp3")
            mixer.music.play(10)
            print("Hey its time to drink glass of water")
            query = input("After drinking water......Type 'W' to stop the music")

            if query == "W":
                water_goal = water_goal + 250
                mixer.music.stop()
                v = time.ctime()
                with open('Water.txt', 'a') as f:
                    f.write('\n You drank water at......')
                    f.write(v)
                print('Log successful')
                break

            else:
                break

        for i in range(1):
            time.sleep(30*60)
            mixer.music.load("Eyes.mp3")
            mixer.music.play()
            print("Hey its time to give to your eyes")
            query = input("After rest......Type 'E' to stop the music")

            if query == "E":
                mixer.music.stop()
                v = time.ctime()
                with open('Eyes.txt', 'a') as f:
                    f.write('\n You took rest at......')
                    f.write(v)
                print('Log successful')
                break

            else:
                pass

        for i in range(1):
            time.sleep(45*60)
            mixer.music.load("Physical.mp3")
            mixer.music.play()
            print("Hey its time for physical activity")
            query = input("After Excercise......Type 'P' to stop the music")

            if query == "P":
                mixer.music.stop()
                v = time.ctime()
                with open('Physical.txt', 'a') as f:
                    f.write('\n You did physical activity at.......')
                    f.write(v)
                print('Log successful')
                break

            else:
                pass
    elif current_time > end_time or current_time < start_time:
        print(" You are out of Office")
        break


print("Thanks for using the Application")
