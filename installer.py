#!/usr/bin/python
import os
if os.path.isfile("/bin/frlinuxploit"):
	print("It is found frlinuxploit is already installed in your system.....Hence removing old one...")
	os.system("rm /bin/frlinuxploit")
elif os.path.isfile("//data/data/com.termux/files/usr/bin/frlinuxploit"):
	print("It is found frlinuxploit is already installed in your system.....Hence removing old one...")
	os.system("rm -rf //data/data/com.termux/files/usr/bin/frlinuxploit")
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
print("\033[5;34 For installing dependencies according to Your Operating system.....")
print("""\033[1;36 
[1] kali linux
[2] parrot os
[3] black arch
[4] termux

 """)
ops=int(input("\033[1;32 CHOOSE YOUR OS : "))
if ops==1:
	os.system("sudo apt-get install python3-pip > /dev/null")
	os.system("sudo python3 -m pip install click")
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
	os.system("sudo apt-get instal python3-pip > /dev/null")
	os.system("sudo python3 -m pip install click")
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
	os.system("sudo python3 -m pip install click")
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
	os.system("apt-get install python3-pip > /dev/null")
	os.system("python3 -m pip install click")
	os.system("apt-get install nmap > /dev/null")
	os.system("apt-get install ncat &> /dev/null") 
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
else:
	print("error:OS is not chosen or Wrong input")






print("STARTING FEBREV LINUxPLOIT......#######################")
os.system("chmod 777 *")
os.system("python3 frlinuxploit.py")
