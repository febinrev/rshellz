#!/bin/bash

#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

if [ "$(id -u)" != "0" ]; then
  echo -e "\n$redColour This Program must run as root$endColour\n"
  exit
else
  clear
  echo -e "$yellowColour

  $yellowColour This Program works with linux $endColour

  $redColour Press <Enter> to continue...$endColour"
  read
  clear

  while true
    do
      echo -e "$yellowColour Retrieving The Wireless connection from history...$endColour"
      sleep 3
      echo -e "$blueColour"
      ls /etc/NetworkManager/system-connections/
      echo -e "$endColour"
      echo -e "$yellowColour-> Total Connections in this Machine $redColour$(ls /etc/NetworkManager/system-connections | wc -l)$endColour$yellowColour ........ $endColour\n"
      echo -e -n "$turquoiseColour Select/Enter the Wi-Fi name :$endColour "
      read wifiName

      if [ "$wifiName" == "0" ]; then
        echo " "
        exit
      fi

      echo -e -n "\n$blueColour The PASSWORD is  ->$endColour $yellowColour"
      sleep 2
      cat /etc/NetworkManager/system-connections/$wifiName | grep psk | tail -n 1 | cut -d '=' -f 2
      sleep 1
      echo -e -n "\n$endColour$blueColour Authentication Type : $endColour$yellowColour"
      sleep 2
      cat /etc/NetworkManager/system-connections/$wifiName | grep key-mgmt | cut -d '=' -f 2
      echo -e "\n$endColour$redColour Press <Enter> to continue...$endColour  "
      read
      clear
  done
fi
