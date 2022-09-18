from machine import Pin,  SPI, I2C
import random
from ssd1306 import SSD1306_I2C
from time import sleep


i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
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
#         
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

oled.text("Lottery numbers.",1,0)
oled.show()

oled.text(str(result[:3]), 0, 10)
oled.text(str(result[3:6]), 0, 20)
oled.text("!!!Good Luck!!!", 0, 32)
oled.show()
print(result)
del result


