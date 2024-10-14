from machine import Pin, PWM

# PWM output at GP2 (pin 4)
pwm = PWM(Pin(2))

pwm.duty_u16(32768)
pwm.freq(100000)


