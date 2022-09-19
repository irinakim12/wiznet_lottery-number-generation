from machine import Pin,  SPI, I2C
import random
from ssd1306 import SSD1306_I2C
from time import sleep
from usocket import socket
import network
import time


result = []

#OLED Setting
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)


def w5x00_init():
#DHCP
    spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
    nic = network.WIZNET5K(spi,Pin(17),Pin(20))
# If you use the Dynamic IP(DHCP), you must use the "nic.active(True)".
# If you use the Static IP, you must use the "nic.ifconfig("IP","subnet","Gateway","DNS")".
    # nic.ifconfig(('192.168.100.13','255.255.255.0','192.168.100.1','8.8.8.8'))
    addr = nic.active(True)
    time.sleep(0.1)
    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())
    return addr[0]
def random_oled():
    global result
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
    oled = SSD1306_I2C(128, 64, i2c)
    oled.text("Lottery numbers.",1,0)
    oled.show()

    oled.text(str(result[:3]), 0, 10)
    oled.text(str(result[3:6]), 0, 20)
    oled.text("!!!Good Luck!!!", 0, 32)
    oled.show()
    print(result)
    #return result
    #del result

def tcp_server(addr):
    global result
    s = socket()
    print(addr)
    s.bind(addr)
    s.listen(1)
    print('listening on', addr)
    while True:
        conn, addr = s.accept()
        print("Connect to:", conn, "address:", addr) 
        print("Loopback server Open!")
        while True:
            data = conn.recv(2048)
            msg = data.decode()
            print('RECEIVED: {} << {}'.format(msg, addr))
            if msg == 'get':
                random_oled()
                conn.send(str(result))
                del result[:6]
                
            
def main():
    get_addr = []
    addr = w5x00_init()
    print(addr)
    get_addr.append(addr)
    get_addr.append(int(5000))
    tcp_server(get_addr)
    
if __name__ == "__main__":
    main()

