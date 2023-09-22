from machine import Pin, Timer
import utime


# Initialize the LED pin as an output

class Led:
    
    def __init__(self):
        self.led = Pin("LED", Pin.OUT)
        self.status = False
        
    def on(self):
        self.led.on()
        self.status = True
        
    def off(self):
        self.led.off()
        self.status = False

    def blink(self, timer):
        self.led.on()
        utime.sleep(0.05)
        self.led.off()
    
    def triple_blink(self):
        if self.status:
            self.led.off()
            utime.sleep(0.1)
        
        for i in range(0, 3):
            self.led.on()
            utime.sleep(0.05)
            self.led.off()
            utime.sleep(0.1)
        
        if self.status:
            self.led.on()
            
    def five_blinks(self):
        if self.status:
            self.led.off()
            utime.sleep(0.1)
        
        for i in range(0, 5):
            self.led.on()
            utime.sleep(0.05)
            self.led.off()
            utime.sleep(0.1)
        
        if self.status:
            self.led.on()            


    def signal(self, duration, freq):
        blink_timer = Timer(freq=freq, mode=Timer.PERIODIC, callback=self.blink)
        start_time = utime.ticks_ms()
        while utime.ticks_diff(utime.ticks_ms(), start_time) < duration * 1000:
            pass
        blink_timer.deinit()
        self.led.off()
        self.status = False
