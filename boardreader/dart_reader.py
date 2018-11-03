from time import sleep
import RPi.GPIO as GPIO
import itertools

from bed_map import BED_MAP

red1=3
red2=5
red3=7
red4=8
red5=10
red6=11
red7=12
red8=15
red9=16
red10=19
red11=21
red12=22

white1=29
white2=31
white3=32
white4=33
white5=35
white6=36
white7=37

#dart_map = {(red1, white1):{"modifier" : "B", "number" : 1, "points" : 1},
#            (red1, white2):{"modifier" : "B", "number" : 2, "points" : 2},
#            (red2, white1):{"modifier" : "B", "number" : 3, "points" : 3},
#            (red2, white2):{"modifier" : "D", "number" : 3, "points" : 6}
#            #TODO Finish him
#           }


class DartReader:
    def __init__(self):
        self.master = [red1, red2, red3, red4, red5, red6,
                       red7, red8, red9, red10, red11, red12]

        self.slave = [white1, white2, white3, white4,
                      white5, white6, white7]
        
        GPIO.setmode(GPIO.BOARD)

        for red in self.master:
            GPIO.setup(red, GPIO.OUT)
            GPIO.output(red, False)

        for white in self.slave:
            GPIO.setup(white, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def read_dart_pins(self):    
        try:
            while(True):
                for red in self.master:
                    GPIO.output(red, True)
                    for white in self.slave:
                        if(GPIO.input(white) == GPIO.HIGH):
                            sleep(.5)
                            return (white, red)
                    GPIO.output(red, False)
        except KeyboardInterrupt as e:
            for red in self.master:
                GPIO.output(red, False)
            raise e

    def read_dart(self):
        return BED_MAP.get(self.read_dart_pins())
