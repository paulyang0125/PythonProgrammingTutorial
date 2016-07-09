import RPi.GPIO as GPIO
from time import sleep

class mylcd:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.CMD_DELAY = 0.0002
        self.CMD_CLEAR_DELAY = 0.001
        self.pin_assignment()
        self.set_GPIOs_write_mode()
    
    def pin_assignment(self):
        self.LCD_RS = 38
        self.LCD_RW = 40
        self.LCD_EN = 29
        self.LCD_D4 = 31
        self.LCD_D5 = 33
        self.LCD_D6 = 35
        self.LCD_D7 = 37
       
    def set_GPIOs_write_mode(self):
        GPIO.setup(self.LCD_EN, GPIO.OUT) # EN
        GPIO.setup(self.LCD_RS, GPIO.OUT) # RS
        GPIO.setup(self.LCD_RW, GPIO.OUT) # RW
        GPIO.setup(self.LCD_D4, GPIO.OUT) # DB4
        GPIO.setup(self.LCD_D5, GPIO.OUT) # DB5
        GPIO.setup(self.LCD_D6, GPIO.OUT) # DB6
        GPIO.setup(self.LCD_D7, GPIO.OUT) # DB7

    def RW_ready(self):
        sleep(0.000001)
        GPIO.output(self.LCD_EN, GPIO.HIGH)
        sleep(0.000001)
        GPIO.output(self.LCD_EN, GPIO.LOW)
    
    def write_lcdcmd(self,cmd):
        GPIO.output(self.LCD_EN, GPIO.LOW) 
        GPIO.output(self.LCD_RS, GPIO.LOW)#tell LCD this is to send commmand
        GPIO.output(self.LCD_RW, GPIO.LOW)
        
        #WRITE higher 4 bits
        GPIO.output(self.LCD_D7,GPIO.HIGH if (0b10000000 & cmd) else GPIO.LOW) #if 7th bit is set, output 1, else set 0 
        GPIO.output(self.LCD_D6,GPIO.HIGH if (0b01000000 & cmd) else GPIO.LOW)
        GPIO.output(self.LCD_D5,GPIO.HIGH if (0b00100000 & cmd) else GPIO.LOW)
        GPIO.output(self.LCD_D4,GPIO.HIGH if (0b00010000 & cmd) else GPIO.LOW)
        self.RW_ready()
        
        #WRITE lower 4 bits
        GPIO.output(self.LCD_D7,GPIO.HIGH if (0b00001000 & cmd) else GPIO.LOW) #if 3th bit is set, output 1, else set 0 
        GPIO.output(self.LCD_D6,GPIO.HIGH if (0b00000100 & cmd) else GPIO.LOW)
        GPIO.output(self.LCD_D5,GPIO.HIGH if (0b00000010 & cmd) else GPIO.LOW)
        GPIO.output(self.LCD_D4,GPIO.HIGH if (0b00000001 & cmd) else GPIO.LOW)
        self.RW_ready()
        sleep(self.CMD_DELAY)
    
    def write_data(self,cmd):
        GPIO.output(self.LCD_RS, GPIO.HIGH)#tell LCD this is to send data 
        GPIO.output(self.LCD_EN, GPIO.LOW) 
        GPIO.output(self.LCD_RW, GPIO.LOW)
        
        #WRITE higher 4 bits
        GPIO.output(self.LCD_D7,GPIO.HIGH if (0b10000000 & cmd) else GPIO.LOW) #if 7th bit is set, output 1, else set 0 
        GPIO.output(self.LCD_D6,GPIO.HIGH if (0b01000000 & cmd) else GPIO.LOW)
        GPIO.output(self.LCD_D5,GPIO.HIGH if (0b00100000 & cmd) else GPIO.LOW)
        GPIO.output(self.LCD_D4,GPIO.HIGH if (0b00010000 & cmd) else GPIO.LOW)
        self.RW_ready()
        
        #WRITE lower 4 bits
        GPIO.output(self.LCD_D7,GPIO.HIGH if (0b00001000 & cmd) else GPIO.LOW) #if 3th bit is set, output 1, else set 0 
        GPIO.output(self.LCD_D6,GPIO.HIGH if (0b00000100 & cmd) else GPIO.LOW)
        GPIO.output(self.LCD_D5,GPIO.HIGH if (0b00000010 & cmd) else GPIO.LOW)
        GPIO.output(self.LCD_D4,GPIO.HIGH if (0b00000001 & cmd) else GPIO.LOW)
        self.RW_ready()
        sleep(self.CMD_DELAY)
    

    def LCD_boot_setup(self):
        #1. EN,RS,RW,D7~D4 都設為 low。
        GPIO.output(self.LCD_D4,0)
        GPIO.output(self.LCD_D5,0)
        GPIO.output(self.LCD_D6,0)
        GPIO.output(self.LCD_D7,0)
        GPIO.output(self.LCD_RS,0)
        GPIO.output(self.LCD_RW,0)
        GPIO.output(self.LCD_EN,0)
        sleep(0.1)
        
        #2. EN 設 high -> 等一下 -> EN 設 low
        GPIO.output(self.LCD_EN,1)
        sleep(0.000001) #wait at least 150ns
        GPIO.output(self.LCD_EN,0)
        sleep(0.000001) #wait at least 150ns
        
        #3.D7~D4分別設為 low, low, high, low (0b0011)
        sleep(0.002)
        self.write_lcdcmd(0x03)
        sleep(0.001) #wait at least 4.1 ms
        self.write_lcdcmd(0x03)
        sleep(0.0001) #wait at least 100 us
        self.write_lcdcmd(0x03)
        sleep(0.0001)
        self.write_lcdcmd(0x02)
        sleep(0.0001)
        # function setup 
        self.write_lcdcmd(0x28) #0010 - set 4bit mode and 1000 - set 2 display lines and 5x8 dot font 設定為4bit操作，兩行顯示模式
        self.write_lcdcmd(0x0c) # 設定為每寫入一次資料，游標位置向右移一格 cursor/display shift
        self.write_lcdcmd(0x01) #清除螢幕並游標歸回原點  CLEAR DISPLAY
        sleep(self.CMD_CLEAR_DELAY) 
        self.write_lcdcmd(0x06) #Enable mode set
        
    def move(self,line,col):
        pos = 0x80 + (line-1) * 0x40 + (col-1)
        self.write_lcdcmd(pos)

    def print_line_1(self,msg):
        self.move(1,1)
        if type(msg) == str:
            for c in msg:
                 self.write_data(ord(c))
                
    def print_line_2(self,msg):
        self.move(2,1)
        if type(msg) == str:
            for c in msg:
                 self.write_data(ord(c))

    def clear_line_1(self):
         self.print_line_1(" " * 16)
        
    def clear_line_2(self):
         self.print_line_2(" " * 16)
        
    def print_msg(self,msg):
        if type(msg) == str:
            for p in range(len(msg)):
                if p < 16:
                     self.write_lcdcmd(0x80 + p)
                     self.write_data(ord(msg[p]))
                elif 15 < p < 32:
                     self.write_lcdcmd(0xc0 + p - 16)
                     self.write_data(ord(msg[p]))
                else:
                    print("error: it's out of bound")
                    break