# Countdown Timer Project 
print("Welcome to countown timer project")

import time

def coundown_timer(seconds):
  while seconds > 0 :
    mins, secs = divmod(seconds, 60)          # mins and seconds calculate kr rhy hain
    time_format = '{:02d}:{:02d}'.format(mins, secs)   # MM:SS format
    print(time_format, end='\r')
    time.sleep(1)              # provide delay
    seconds -= 1
 
  print("00:00 \n Time's Up")


# user input for timer
total_sec = int(input("Enter time in seconds for countdown:"))
coundown_timer(total_sec)