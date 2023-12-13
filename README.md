# rShellZ

### rShellZ is a linux exploitation assistance framework made for Pentesters and Hacking Learners
## It is Mainly aimed for educational purposes , learn Pentesting
### It could be more helpful in CTF challenges

# Usage:
    1. Download and extract rShellz
    2. Go to the directory
    3. Open Terminal
    4. $ chmod +X *
    5. $ ./installer
    6. $ ./rShellz.py   or python3 rShellz.py
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
    whoami / current_user                          ----------> returns Current user
    sysinfo / systeminfo /machine_info             ----------> returns Info about the Local Machine
    
# Available Modules:
[*] Auxiliary:
---------------------------------------------------------------------------------------------------------
    0)                    auxiliary-enum_ssh_info                  Enumerates Information about SSH 
    1)                    auxiliary-port_scan                      Scans all the ports and detects the service
    2)                    auxiliary-http_banner_grab               grabs HTTP server banner  


[*] Payloads:
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
    13)    payload-telnet_reverse_tcp          spawns a reserse tcp shell using telnet
----------------------------------------------------------------------------------------------------------

Handler:
----------------------------------------------------------------------------------------------------------

    99)       tcp_handler                          Handles all the reverse connections

----------------------------------------------------------------------------------------------------------





[*] Post Exploitation, Privilege Escalation & Enumeration :
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
    24)         post/mimipenguin                         extracts Clear text Password of current user from memory(root)
    25)         post/gather_wifi_creds                   gets wireless credentials saved in the local machine(root)
    26)         post/linuxprivchecker                    python script to check privesc vulnerabilities
    27)         post/crack_shadow_hash                   cracks hashes which are retrieved from /etc/shadow
    28)         post/crack_grub2_pbkdf2                  cracks hashes generated by GRUB2(grub-mkpasswd-pbkdf2)
    29)         post/clear_track                         command to clear the tracks in victim machine
   
[*]SPECIAL REVERSE_SHELL ENCRYPTED:
----------------------------------------------------------------------------------------------------------
    30)         openssl_reverse_tcp                      Reverse tcp encrypted shell with openssl
    31)         ssl_listener                             handler for the openssl payload
    
[*] PHP WEB-SHELLS:
----------------------------------------------------------------------------------------------------------

    29)         php_webshell                             Simple php webshell with password authentication
    30)         php_webshell_gui                         A simple interactive webshell
    31)         webshell_handler                         Handler for simple php webshell which connects and executes commands
   
 [*] STRING ENCODERS:
 ----------------------------------------------------------------------------------------------------------
    35)         base64_encoder                  Encodes specified string with base64 encoding
    36)         base32_encoder                  Encodes specified string with base32 encoding
    37)         hex_encoder                     Encodes specified string in Hex
    38)         url_encoder                     Encodes specified string in url encoding
    39)         rot13_encoder                   Encodes specified string in rot13 algorithm 

### [*] GTFOBINS:

    Available Commands:

    help gtfobins                     To see the list of gtfobins binaries 
    gtfobins <binary name>             To see the binary and its usage/methods from gtfobins
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
