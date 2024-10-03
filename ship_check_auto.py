##################################################
#Automation of Ship Check
#10/02/24
#Efrain Alvarez
##################################################

from re import findall
from subprocess import Popen, PIPE

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
            
ships = ["www.google.com", "8.8.8.8", "www.youtube.com", "www.facebook.com"]

ping(ships,4)