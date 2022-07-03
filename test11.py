#Q11.Write a code to check ip address of your system.

from requests import get
ip = get("https://api.ipify.org").text
print("Current IP address of my system is: ",ip)