#Security Shephard Setup for Software Security classes

import fileinput
import re
import sys
import os
from sys import platform
print("select linux if your using ubuntu or kali linux")
system = input("please enter your system (linux/arch)")
if system == "linux":
    print("updating repositories")
    os.system("sudo apt-get update")
    print("installing Security shephard dependencies")
    os.system("sudo apt-get install git maven docker docker-compose default-jdk -y")
    print("downloading securityshepherd from github ")
    print("original link: https://github.com/OWASP/SecurityShepherd")
    os.system("sudo gpasswd -a $USER docker")
    os.system("cd SecurityShepherd")
    os.system("mvn -Pdocker clean install -DskipTests")
    os.system("docker-compose up -d")
if system == "arch":
    os.system("work in progress")

