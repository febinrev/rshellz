import os
import socket
os.system("su")
os.system("apt-get install openssh > /dev/null")
print("""
FEBREV-LINUXPLOIT  
          --->Port Forwarding Module using ssh serveo.net

     coded By: Febin Rev
""")
port=input("ENTER THE PORT YOU USED IN THE PAYLOAD TO FORWARD OVER INTERNET : ")
print(f"PORT FORWARDING ENABLED ON PORT >>> {port}")
print("CTRL-C TO STOP,,,,,TERMINATING THIS CAN STOP PORT FORWARDING")
os.system(f"ssh -R {port}:localhost:{port} serveo.net")

