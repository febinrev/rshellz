#!/usr/bin/python
import os
if os.path.isfile("/bin/frlinuxploit"):
  os.system("rm /bin/frlinuxploit")
else:
  print("........................................................................................................")
print("""
███████╗███████╗██████╗ ██████╗ ███████╗██╗   ██╗                     
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║   ██║                     
█████╗  █████╗  ██████╔╝██████╔╝█████╗  ██║   ██║                     
██╔══╝  ██╔══╝  ██╔══██╗██╔══██╗██╔══╝  ╚██╗ ██╔╝                     
██║     ███████╗██████╔╝██║  ██║███████╗ ╚████╔╝                      
╚═╝     ╚══════╝╚═════╝ ╚═╝  ╚═╝╚══════╝  ╚═══╝                       
                                                                      
██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗ 
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                      
""")
print("installing dependencies.....")
print("""
[1] kali linux
[2] parrot os
[3] black arch
[4] termux

 """)
ops=int(input("CHOOSE YOUR OS : "))
if ops==1:
	os.system("sudo apt-get install nmap > /dev/null")
	os.system("sudo apt-get install ncat > /dev/null") 
	path=os.getcwd()
	with open("frlinuxploit.sh","w+") as fr:
	      fr.write(f"python3 {path}/frlinuxploit.py.py")
	os.system(f"cp {path}/frlinuxploit.sh /bin/frlinuxploit")
	os.system("chmod +x /bin/frlinuxploit")
	print("")
	print("NOW YOU CAN RUN FEBREV-LINUXPLOIT FRAMEWORK FROM ANYWERE BY TYPING COMMAND  >>  frlinuxploit")
	exiting=input("ENTER ANY KEY TO CONTINUE.......!!!!! ")
	print(" ")
	print(" ")
	print(" ")

elif ops==2:
	os.system("sudo apt-get install nmap > /dev/null")
	os.system("sudo apt-get install ncat > /dev/null") 
	path=os.getcwd()
	with open("frlinuxploit.sh","w+") as fr:
	      fr.write(f"python3 {path}/frlinuxploit.py.py")
	os.system(f"cp {path}/frlinuxploit.sh /bin/frlinuxploit")
	os.system("chmod +x /bin/frlinuxploit")
	print("")
	print("NOW YOU CAN RUN FEBREV-LINUXPLOIT FRAMEWORK FROM ANYWERE BY TYPING COMMAND  >>  frlinuxploit")
	exiting=input("ENTER ANY KEY TO CONTINUE.......!!!!! ")
	print(" ")
	print(" ")
	print(" ")
elif ops==3:
	os.system("sudo pacman -S install nmap > /dev/null")
	os.system("sudo pacman -S install ncat > /dev/null") 
	path=os.getcwd()
	with open("frlinuxploit.sh","w+") as fr:
	      fr.write(f"python3 {path}/frlinuxploit.py.py")
	os.system(f"cp {path}/frlinuxploit.sh /bin/frlinuxploit")
	os.system("chmod +x /bin/frlinuxploit")
	print("")
	print("NOW YOU CAN RUN FEBREV-LINUXPLOIT FRAMEWORK FROM ANYWERE BY TYPING COMMAND  >>  frlinuxploit")
	exiting=input("ENTER ANY KEY TO CONTINUE.......!!!!! ")
	print(" ")
	print(" ")
	print(" ")
elif ops==4:
	os.system("sudo apt-get install nmap > /dev/null")
	os.system("sudo apt-get install ncat > /dev/null") 
	path=os.getcwd()
	with open("frlinuxploit.sh","w+") as fr:
	      fr.write(f"python3 {path}/frlinuxploit.py")
	os.system(f"cp {path}/frlinuxploit.sh //data/data/com.termux/files/usr/bin/frlinuxploit")
	os.system("chmod +x //data/data/com.termux/files/usr/bin/frlinuxploit")
	print("")
	print("NOW YOU CAN RUN FEBREV-LINUXPLOIT FRAMEWORK FROM ANYWERE BY TYPING COMMAND  >>  frlinuxploit")
	exiting=input("ENTER ANY KEY TO CONTINUE.......!!!!! ")
	print(" ")
	print(" ")
	print(" ")






print("STARTING FEBREV LINUxPLOIT......#######################")
os.system("chmod +x *")
os.system("sudo python3 frlinuxploit.py")
