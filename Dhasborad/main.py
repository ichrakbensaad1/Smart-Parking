import RPi.GPIO as GPIO
import time
from flask import Flask, request, render_template, redirect, url_for, jsonify

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

triggerPin = 23
echoPin = 24
#buzzer = 18
#led = 15

GPIO.setup(triggerPin,GPIO.OUT)
GPIO.setup(echoPin,GPIO.IN)
#GPIO.setup(buzzer,GPIO.OUT)
#GPIO.setup(led,GPIO.OUT)
#GPIO.output(buzzer,GPIO.LOW)


@app.route("/")
def index():
   return render_template("index1.html")
        

      
@app.route("/listening", methods = ['GET','POST'])
def listening():
    distance = 0
    while True:
        GPIO.output(triggerPin, False)
        time.sleep(2)
        
        GPIO.output(triggerPin, True)
        time.sleep(0.00001)
        GPIO.output(triggerPin, False)
        
        while GPIO.input(echoPin)==0:
            pulseStart = time.time()   
        
        while GPIO.input(echoPin)==1:
            pulseEnd = time.time()
            
        pulseDuration = pulseEnd - pulseStart
        
        distance = round(pulseDuration * 17150 , 2)
        print(distance)
        if  distance < 20:
            #GPIO.output(led,GPIO.HIGH)
            #GPIO.output(buzzer,GPIO.HIGH)
            
            
            
            return jsonify({'Occupe':1,'Distance':distance})
            
        else:
            #GPIO.output(buzzer,GPIO.LOW)
            #GPIO.output(led,GPIO.LOW)
            return jsonify({'Occupe':0,'Distance':distance})
        


if __name__ == "__main__":
    app.run()