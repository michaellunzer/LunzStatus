#! python
from pushbullet import PushBullet
import time
import re
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

GPIO.setwarnings(False) 

pb = PushBullet('o.u5oBajWZhOAptaA3UkvSXy7UgMdKerHG')

##EXAMPLE Pushbullet options##
#print(pb.devices)
# push = pb.push_note("This is the title", "This is the body")
# push = pb.push_link("Cool site", "https://github.com")

pushes = pb.get_pushes()

latest = pushes[0]

#print(latest) #prints the latest pushbullet notification

body = latest.get('body')

#print(body) #prints the body of the latest notification

if re.search('HOME', body):
	print("Michael is home!")
	GPIO.output(18, GPIO.HIGH)
	GPIO.output(23, GPIO.LOW)
elif re.search('WORK', body):
	print("Michael is at Work")
	GPIO.output(18, GPIO.LOW)
	GPIO.output(23, GPIO.HIGH)
else:
	print("Michael is away")
	GPIO.output(18, GPIO.LOW)
	GPIO.output(23, GPIO.HIGH)

#GPIO.cleanup()  # when this is off, the LED turns off after the program runs
