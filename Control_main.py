from RPIO import PWM

throttle = PWM.Servo()
yaw = PWM.Servo()
altitude_hold = PWM.Servo()

# Clear servo on GPIO17
# throttle.stop_servo(17)

def forward():
  throttle.set_servo(17, 1200)

def turn(int degree):
  yaw.set_servo(15, degree)
  
def main():
  # For altitude hold (channel 5 on receiver)
  altitude_hold.set_servo(16, 1500)
  if (forward = true)
    forward()
  if (turn = true)
    turn()

main()



