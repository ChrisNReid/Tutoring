#Speed Tracker

# take input of time 1
# take input of time 2
# take input of distance between
# calculate average speed

def speedtracker(time1, time2, distance):
  # speed = distance/time

  time = time2-time1
  speed = distance/time
  print(speed,"m/s")
  kmphspeed = speed*3.6
  print(kmphspeed,"kmph")
  mphspeed = kmphspeed/1.6
  print(mphspeed, "mph")
  
speedtracker(0, 60, 1000)