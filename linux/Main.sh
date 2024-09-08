#!/bin/bash

blue="\e[0;94m"
green="\e[0;92m"
reset="\e[0m"
yellow="\e[0;33m"

echo -e "${green}updating..."
./Update.sh
echo -e "${yellow}Welcome to V1.2 of the FreeSearcher CLI ${green}Linux Edition"
echo -e "${yellow}enter your prompt:${reset}"

read location

chmod u+x $location.sh

./$location.sh
