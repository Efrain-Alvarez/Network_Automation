import subprocess

def ping_test(list):
    for ship in list:
        response = (subprocess.run(['ping','-c','4',ship], text=True))
        print(type(response))

test_list = ['www.google.com', 'www.youtube.com']

ping_test(test_list)