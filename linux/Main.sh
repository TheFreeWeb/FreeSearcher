#!/bin/bash

blue="\e[0;94m"
green="\e[0;92m"
reset="\e[0m"
yellow="\e[0;33m"

echo -e "${green}Updating..."
chmod u+x update.sh
chmod u+x goob.sh
./update.sh


echo -e "${blue}Do you wish to see the availible downloads? [Yy,Nn] ${green}"
read answer

if [ "$answer" != "${answer#[Yy]}" ] ;then
    find . -type f -name "*.sh"
fi


echo -e "${yellow}Welcome to V1.4 of the FreeSearcher CLI ${blue}Linux Edition"
echo -e "${yellow}enter your command:${blue}"

read location

chmod u+x $location.sh

./$location.sh
