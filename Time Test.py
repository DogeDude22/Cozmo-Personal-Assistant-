import cozmo
import datetime

currentDT = datetime.datetime.now()
  
def main_program(robot: cozmo.robot.Robot):

robot.say_text((currentDT.strftime("%I:%M:%S %p"))).wait_for_completed()

cozmo.run_program(main_program)