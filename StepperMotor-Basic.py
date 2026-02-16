from machine import Pin,
import time

step1 = Pin(18,Pin.OUT)
step2 = Pin(19,Pin.OUT)
step3 = Pin(22,Pin.OUT)
step4 = Pin(23,Pin.OUT)

while True:
    step1.value(1)
    step2.value(1)
    step3.value(0)
    step4.value(0)
    time.sleep_ms(3)

    step1.value(0)
    step2.value(1)
    step3.value(0)
    step4.value(0)
    time.sleep_ms(3)
    
    step1.value(0)
    step2.value(1)
    step3.value(0)
    step4.value(0)
    time.sleep_ms(3)

    step1.value(0)
    step2.value(1)
    step3.value(0)
    step4.value(0)
    time.sleep_ms(3)
