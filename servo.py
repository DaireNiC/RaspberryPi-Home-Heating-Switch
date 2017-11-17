import RPi.GPIO as GPIO
from time import sleep
#set up GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)
pwm=GPIO.PWM(03, 50)
pwm.start(0)
#funstion that moves the servo (90 degrees max)
def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(03, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(03, False)
	pwm.ChangeDutyCycle(0)
#call the servo
SetAngle(90) 
#wind down gracefully
pwm.stop()
GPIO.cleanup()