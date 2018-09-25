import time
import cozmo 
x = 0

def countdown(n) :
while n > 0:
print (n)
n = n - 1
if n ==0:
  x = 1
  print("Timer's up!")
countdown(15)

def cozmo_set(robot: cozmo.robot.Robot):
  
  if x = 1
    robot.say_text("Timer's up!").wait_for_completed()
