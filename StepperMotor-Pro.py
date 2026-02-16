from machine import Pin
import time

step1 = Pin(18,Pin.OUT)
step2 = Pin(19,Pin.OUT)
step3 = Pin(22,Pin.OUT)
step4 = Pin(23,Pin.OUT)
list1=[[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]
list2=[[1,0,0,1],[0,0,1,1],[0,1,1,0],[1,1,0,0]]

while True:
    for r in range(500):
        for i in list1:
            step1.value(i[0])
            step2.value(i[1])
            step3.value(i[2])
            step4.value(i[3])
            time.sleep_ms(3)
        
    for r in range(500):
        for i in list2:
            step1.value(i[0])
            step2.value(i[1])
            step3.value(i[2])
            step4.value(i[3])
            time.sleep_ms(3)


