import os
import socket
import click
os.system("su")
os.system("apt-get install openssh > /dev/null")
print("""
FEBREV-LINUXPLOIT  
          --->Port Forwarding Module using ssh serveo.net

     coded By: Febin Rev
""")
port=input("ENTER THE PORT YOU USED IN THE PAYLOAD TO FORWARD OVER INTERNET : ")
print("[1] serveo.net       [2] localhost.run")
vendor=click.prompt("Enter the portforwarding platform :", type=int, default=2)
if vendor==1:
          print(f"PORT FORWARDING ENABLED ON PORT >>> {port}")
          print("CTRL-C TO STOP,,,,,TERMINATING THIS CAN STOP PORT FORWARDING")
          os.system(f"ssh -R {port}:localhost:{port} serveo.net")
elif vendor==2:
          print(f"PORT FORWARDING ENABLED ON PORT >>> {port} ")
          print("CTRL-C TO STOP,,,,TERMINATING THIS CAN STOP PORT FORWARDING")
          os.system(f"ssh -R {port}:localhost:{port} localhost.run")
else:
          print("WRONG INPUT....going for default")
          print(f"PORT FORWARDING ENABLED ON PORT >>> {port} ")
          print("CTRL-C TO STOP,,,,TERMINATING THIS CAN STOP PORT FORWARDING")
          os.system(f"ssh -R {port}:localhost:{port} localhost.run")
