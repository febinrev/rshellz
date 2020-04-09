# Febrev-Linuxploit

### Febrev-linuxploit is a linux exploitation assistance framework made for Pentesters and Hacking Learners
## It is Mainly aimed for educational purposes , learn Pentesting
### It could be more helpful in CTF challenges

# Usage:
    1. Download and extract febrev-linuxploit
    2. Go to the directory
    3. Open Terminal
    4. $ chmod +X *
    5. $ ./installer
    6. $ ./febrev-linuxploit.py   or python3 febrev-linuxploit.py
    7. Linuxploit console will open up
    8. Type   help  to get all available commands and module info
    
# Available Commands:
    help                                           ----------> shows help message
    use <module name | module s.no>                ----------> to use the module
    banner                                         ----------> to change banner of linuxploit
    bannerq / clear                                ----------> to clear the console
    os:<command>                                   ----------> to execute an os command
    exec:<command>                                 ----------> to execute an os command
    exec <command>                                 ----------> to execute an os command
    os <command>                                   ----------> to execute an os command
    quit / exit                                    ----------> to exit from the console
    
# Available Modules:
[*] Auxiliary:
---------------------------------------------------------------------------------------------------------
S.no:                |       Auxiliary module               |         Description
---------------------------------------------------------------------------------------------------------
0)                    auxiliary-enum_ssh_info                  Enumerates Information about SSH 
1)                    auxiliary-port_scan                      Scans all the ports and detects the service
2)                    auxiliary-http_banner_grab               grabs HTTP server banner  


[*] Payloads:
----------------------------------------------------------------------------------------------------------
S.no:  | payload module                |             Description
----------------------------------------------------------------------------------------------------------
3)     payload-binary_shell_reverse_tcp    linux reverse tcp shell binary
4)     payload-bash_reverse_tcp            Bash reverse tcp shell payload
5)     payload-perl_reverse_tcp            perl reverse tcp shell payload
6)     payload-python_reverse_tcp          php reverse tcp shell payload
7)     payload-php_reverse_tcp             python reverse tcp shell payload
8)     payload-ruby_reverse_tcp            ruby reverse tcp shell payload
9)     payload-socat_reverse_tcp           socat reverse tcp shell payload
10)    payload-netcat_reverse_tcp          netcat reverse tcp shell payload
11)    payload-lua_reverse_tcp             lua reverse tcp shell payload
12)    payload-curl_reverse_tcp            spawns a Reverse tcp shell using curl
----------------------------------------------------------------------------------------------------------

Handler:
----------------------------------------------------------------------------------------------------------
S.no:    |    Handler                     |               Description
----------------------------------------------------------------------------------------------------------

13)       tcp_handler                          Handles all the reverse connections

----------------------------------------------------------------------------------------------------------





[*] Post Exploitation, Privilege Escalation & Enumeration :
----------------------------------------------------------------------------------------------------------
S.no:     |         Post module               |          Description
----------------------------------------------------------------------------------------------------------

14)         post/LinEnum                             Enumerates the informations about local machine
15)         post/linpeas                             Enumerates the informations of local machine
16)         post/pspy                                Enumerates the live background processes in the local machine without root privileges
17)         post/unix-privesc-check                  Unix/Linux privilege escalation checker
18)         post/linux-exploit-suggester             Linux local exploit suggester
19)         post/logrotten                           Exploits logrotate process
20)         post/spawn_shell                         Gives commands to spawn stable tty command-shell
21)         post/nc_portfwd_pivot                    netcat portforwarding for pivoting
22)         post/ssh_local_portfwd                   ssh local portforward for pivoting
23)         post/ssh_remote_portfwd                  ssh remote portforward for pivoting 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
