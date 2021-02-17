#Security Shephard Setup for Software Security classes

import fileinput
import re
import sys
import os
from sys import platform
print("please make sure you are using python3")
print("to install python3, run : sudo apt-get install python3")
print("select linux if your using ubuntu or kali linux")
system = input("please enter your system (linux/arch)")
if system == "linux":
    print("updating repositories")
    os.system("sudo apt-get update")
    print("installing Security shephard dependencies")
    os.system("sudo apt-get install git maven docker docker-compose default-jdk -y")
    print("downloading securityshepherd from github ")
    os.system("git clone https://github.com/OWASP/SecurityShepherd.git")
    print("original link: https://github.com/OWASP/SecurityShepherd")
    os.system("sudo gpasswd -a $USER docker")
    os.chdir("SecurityShepherd")
    os.system("mvn -Pdocker clean install -DskipTests")
    os.system("docker-compose up -d")
    print("SecurityShepherd is running in the background in a docker container")
    print("To Stop SecurityShepherd please run this command below")
    print("Enter docker-compose down in this current directory")
    print("to view all current docker containers run: docker ps -a")
    print("Go to http://127.0.0.1")
if system == "arch":
    os.system("work in progress")

