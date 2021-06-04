import RPi.GPIO as GPIO
import time

trig_pin=7
echo_pin   =11
motsol_i=16
motsol_g=18

motsag_i=13
motsag_g=15

GPIO.setmode(GPIO.BOARD)

GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

GPIO.setup(motsol_i, GPIO.OUT)
GPIO.setup(motsol_g, GPIO.OUT)
GPIO.setup(motsag_i, GPIO.OUT)
GPIO.setup(motsag_g, GPIO.OUT)

baslangicZamani= 0
bitisZamani    = 0


def ileri():
    GPIO.output(motsol_i, 1)
    GPIO.output(motsol_g, 0)
    GPIO.output(motsag_i, 1)
    GPIO.output(motsag_g, 0)
    
def geri():
    GPIO.output(motsol_i, 0)
    GPIO.output(motsol_g, 1)
    GPIO.output(motsag_i, 0)
    GPIO.output(motsag_g, 0)

def sag():
    GPIO.output(motsol_i, 1)
    GPIO.output(motsol_g, 0)
    GPIO.output(motsag_i, 0)
    GPIO.output(motsag_g, 1)
    
def sol():
    GPIO.output(motsol_i, 0)
    GPIO.output(motsol_g, 1)
    GPIO.output(motsag_i, 1)
    GPIO.output(motsag_g, 0)
    
def dur():
    GPIO.output(motsol_i, 0)
    GPIO.output(motsol_g, 0)
    GPIO.output(motsag_i, 0)
    GPIO.output(motsag_g, 0)
    
while True:
    GPIO.output(trig_pin, True)
    time.sleep(0.001)
    GPIO.output(trig_pin, False)
    
    if GPIO.input(echo_pin) == 0:
        baslangicZamani= time.time()
    
    if GPIO.input(echo_pin) == 1:
        bitisZamani= time.time()

    zamanFarki= bitisZamani - baslangicZamani

    mesafe= (34300*zamanFarki)/2
    print(mesafe)


    if (mesafe<30):
        sag()
    else:
        ileri()
    
        
    
    