from machine import Pin,  SPI, I2C
import ssd1306
import random
result = []
#for i in range(6):
#    num = random.randrange(1,46)
#    print(num , result)
#    if num in result:
#        num = random.randrange(1,46)
#        result.insert(0,num)
#        print("%d Again\r\n "%i)
#    else:
#        result.insert(0,num)
i2c = I2C(sda=machine.Pin(23), scl=machine.Pin(22))
i2c.scan()
        
while True:
    num = random.randrange(1,46)
    if num in result:
        num = random.randrange(1,46)
        result.insert(0,num)
       # print("Again\r\n ")
    else:
        result.insert(0,num)
    if 6 == len(result):
        break
result.sort() 
print(result)
del result