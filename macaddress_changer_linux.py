import subprocess
def change_mac_address(interface,new_mac_address):
    subprocess.call(["ifconfig",interface,'down'])
    subprocess.call(["ifconfig","hw",new_mac_address])
    subprocess.call(["ifconfig","up"])





def main():
    interface = str(input("[*]ENTER YOUR INTERFACE TO CHANGE:"))
    new_mac_address = input("[*]ENTER YOUR NEW MAC ADDRESS:")


    before_change = subprocess.check_output(["ifconfig",interface])
    change_mac_address(interface,new_mac_address)
    
    after_change = subprocess.check_output(["ifconfig"])

    if before_change == after_change:
        print(f"your mac address is not changed{new_mac_address}")
    else:
        print(f"mac address is successfully changed on interface {interface} to {new_mac_address}")
main()