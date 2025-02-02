import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(2.5)

##try:
##    while True:
##        p.ChangeDutyCycle(7.5)  # turn towards 90 degree
##        time.sleep(1) # sleep 1 second
##        p.ChangeDutyCycle(2.5)  # turn towards 0 degree
##        time.sleep(1) # sleep 1 second
##        p.ChangeDutyCycle(12.5) # turn towards 180 degree
##        time.sleep(1) # sleep 1 second 
##except KeyboardInterrupt:
##    p.stop()
##    GPIO.cleanup()

for i in range (1,19):
    p.ChangeDutyCycle(2.5+(0.0555*i*10))
    time.sleep(1)
    print(2.5+(0.0555*i*10))

p.stop()
GPIO.cleanup()
