import requests
import os
import sys
import time
from colorama import Fore

os.system("clear")
print(Fore.LIGHTRED_EX+"""
 ********************************************************************
 *          _______           _     _________ _______  _______      *
 *         (  ___  )|\     /|( \    \__   __/(  ____ \(  ____ )     *
 *         | (   ) || )   ( || (       ) (   | (    \/| (    )|     *
 *         | |   | || | _ | || | _____ | |   | |      | (____)|     *
 *         | |   | || |( )| || |(_____)| |   | |      |  _____)     *
 *         | |   | || || || || |       | |   | |      | (           *
 *         | (___) || () () || (____/\ | |   | (____/\| )           *
 *          _______)(_______)(_______/ )_(   (_______/|/            *
 ====================================================================
 **                     Developer : OWL                            **
 **                   Channel : @UltraOwl                          **
 ====================================================================          
          """)   
print(Fore.BLUE+" *************************")

while True:
	print(Fore.YELLOW+" [*][*]Click ctrl+c to exit from program")
	url = input(Fore.CYAN+" Enter url for <TCP PORT SCAN>: ")

	print(Fore.WHITE+" [*]Progress...")
	req = requests.get("https://api.hackertarget.com/nmap/?q="+url, stream=True)
	sys.stdout.write("\033[F")

	print(Fore.MAGENTA+" >>results for <"+url+">:")

	if "Error enter single IP or Host only on Free Scan" in req.text:
		print(Fore.RED+" [*] PLEASE ENTER VAILD ADDRESS!")

	elif "API count exceeded - Increase Quota with Membership" in req.text:
		print(Fore.RED+" [*][*] OH!!! You're BANNED from the server!")
		print(Fore.RED+" [*][*] You can try later or change your ip address to not BANNED ip address!")
	else:
		for line in req.iter_lines():
			st = str(line)
			if "PORT" in st:
				print(Fore.YELLOW+" "+st[2:len(st)-1])
			elif "tcp" in st:
				print(Fore.GREEN+" "+st[2:len(st)-1])

	print(" |\n |\n |")
	print(Fore.BLUE+" *************************")
