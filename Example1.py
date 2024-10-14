from machine import Pin

led = Pin(0, Pin.OUT)
button = Pin(1, Pin.IN, Pin.PULL_UP)

while True:
    if button.value()==0:
        led.on()
                
    if button.value()==1:
        led.off()



        
        






