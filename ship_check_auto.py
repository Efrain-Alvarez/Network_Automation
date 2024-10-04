##################################################
#Automation of Ship Check
#10/02/24
#Efrain Alvarez
##################################################

from re import findall
from subprocess import Popen, PIPE
import os

def ping (host,ping_count):

    for ip in host:
        data = "" #empty string, holds response of ping test
        output= Popen(f"ping {ip} -n {ping_count}", stdout=PIPE, encoding="utf-8")

        for line in output.stdout:
            data = data + line #stdout 
            ping_test = findall("TTL", data) #list of TTL ['TTL', 'TTL', 'TTL', 'TTL']
        if ping_test:
            print(f"{ip} : Successful Ping")
            start_point = data.find("Ping statistics")
            print(data[start_point:].strip())
            #output to text file
            output_file = open("test.txt", "a")
            output_file.write(data[start_point:].strip())
            output_file.write('\n\n============================================================\n\n')
            output_file.close()
        else:
            print(f"{ip} : Failed Ping")
            output_file = open("test.txt", "a")
            output_file.write(data[start_point:].strip())
            output_file.write('\n\n============================================================\n\n')
            output_file.close()


dir_path = r'D:\efrai\Documents\ReservationApp'

try:
    file_count = len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))])
    print(f'File count: {file_count}')
except FileNotFoundError:
    print(f"The directory '{dir_path}' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
            
#ships = ["192.168.4.1", "8.8.8.8", "www.google.com", "192.168.4.5"]

#ping(ships,4)