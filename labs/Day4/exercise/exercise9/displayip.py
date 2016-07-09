from subprocess import check_output
from mylcd import mylcd
from time import sleep

def get_hostname():
    return check_output('hostname').decode().strip('\n')
    
    
def get_ips():
    ip_data = check_output('ifconfig').decode().split()
    ip_list = []
    for item in ip_data:
        if "addr:" in item:
            ip_list.append(item[5:])
    return [i for i in ip_list if i]

    
if __name__ == '__main__':
    myLCD = mylcd()
    myLCD.LCD_boot_setup()
    myLCD.clear_line_1()
    while(True):
        myLCD.clear_line_1()
        myLCD.print_line_1(get_hostname())
        ip_list = get_ips()
        for i in ip_list :
            myLCD.clear_line_2()
            myLCD.print_line_2(i)
            sleep(1)
