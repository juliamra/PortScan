from Project.pyportscan import *
from termcolor import colored
from art import text2art 
from time import sleep


banner = text2art("PyPortScanner", font="slant")
colored_banner = colored(banner, color="green")
print(colored_banner)
sleep(0.6)
print("\033[1;35m-The scanner is programmed to scan all ports. If you want to change this, do it in the main.py file. If you want to scan a specific port, you will need to modify the program logic in the pyportscan.py file\033[m")
sleep(0.6)
print("\033[1;34m-The scanner results will be available in the file scan_results.txt\033[m")
sleep(0.6)
host = input("\033[1;36mHost: \033[m")
sleep(0.7)
print("\033[1;36mProcessing...\033[m")
sleep(0.7)

if __name__ == "__main__":
    hostname = host
    port_range = range(1, 65537)  
    output_file = "scan_results.txt"  
    scanner = PortScanner(hostname, port_range)
    try:
        print(f'\033[1;36mStarting target port scan {hostname}\033[m')
        results = scanner.run_scan()
        scanner.save_results(results, output_file)
        print(f"\033[1;32mResults saved in {output_file}\033[m")
    except Exception as e:
        print("\033[1;31mAlvo não encontrado\033[m")
        print(f"\033[1;31mErro: {e}\033[m")