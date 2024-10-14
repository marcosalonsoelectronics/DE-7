from machine import Pin, Timer

led = Pin(0, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=5, mode=Timer.PERIODIC, callback=blink)



