#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports.
import sys # System.
import time # The time.
import os # Operating System functions.
import subprocess # So we can call other scripts!
import re # Regular expression, because we all love that... right?
import argparse # Google said I needed this.
import core.shepherd_logo as logo # My logo, of course.
import core.colors as colors # We all love a splash of color.
import core.mods as mods # So we can let people modify it easier!

# List of commands.
parser = argparse.ArgumentParser()
ap = parser.add_mutually_exclusive_group()
ap.add_argument('--cli', help='Run the Command Line version of Shepherd-Project', action='store_true') # Developing.
ap.add_argument('--pingreq', help='Is it alive, is it dead? | Shepherd-Project', action='store_true') # Setup and working.
ap.add_argument('--vulncheck', help='From the infamous Log4j, to heartbleed and a mass port-scan on a public IP - youll know where to hit them where it hurts | Shepherd-Project', action='store_true') # Developing.
ap.add_argument('--whoisrec', help='This will give you public record information about a domains owner, nameservers, etc | Shepherd-Project', action='store_true') # Further research needed.
ap.add_argument('--cryptex', help='Utilise the CrypteX package developed by Cythes @ https://github.com/AlexKollar | Shepherd-Project', action='store_true') # Awaiting Alex.
ap.add_argument('--p-vpn', help='Connect and Disconnect from ProtonVPN through the P-VPN Feed option | Shepherd-Project', action="store_true") # Further research needed.
ap.add_argument('-v', '--version', help='Version', action="version", version='2.0.1') # Setup and working.
args = vars(parser.parse_args())

# Fair warning notice before it runs.
notice = f'''
#  {colors.bcolors.RED}Please read the following information carefully before using this tool:{colors.bcolors.ENDC}
#  The content of the this repository is for educational purposes and uses only, or in a professional capacity.
#  Do not use this tool excessively, as port-scanning, OSInt and Dorking might be legal but using the functionality for:
#  Cyber terrorism, cyber thefts and other malicious activities is illegal - outright!
# 
#  Using this tool is not anonymous and one needs to be aware that Google knows who you are as does the ISP you utilise,
#  and from where and when you perform these searches - even in some cases when using the built in ProtonVPN connection function.{colors.bcolors.ENDC} 
# 
#  {colors.bcolors.RED}DO YOU AGREE TO TO OUR TERMS AND CONDITIONS?{colors.bcolors.ENDC} (STATE: Y/N) THEN PRESS "ENTER"
'''

# Start of menu script caller.

def shepherd_menu():
    global ch
    mods.clear_screen()
    logo.shepherd_logo()
    print(f'''
CHOOSE OPTION :

    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Ping Request    (Working)     [x]
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Vuln Checking   (Developing)  [x]
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} Who Is Record   (Working)     [x]
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} CrypteX         (Waiting)     [x]
    {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} ProtonVPN Cnct  (Developing)  [x]
    ''')

    ch = int(input("    --> "))
    print('\n\n')


# PingReq

if args['pingreq']:
    logo.shepherd_logo() # Prints the Logo.
    print(notice) # Prints the notice seen above, again, if the screen was cleared.
    yn = input()
    if yn == 'y' or yn =='Y':  ## MY CODE ##
        while True:
            print("\n") # Adds a break in the lines
            pingreq_ip_entered = input("\nPlease enter the ip address that you want to ping: ") # Just asks you to give the program what IP you want to ping.
            print("\n") # Adds a break in the lines
            print(f"{pingreq_ip_entered} is the entered IP!") # Let's you know the IP was accepted for use.
            print("\n") # Adds a break in the lines
            break
            
        while True:
            os.system(f"ping {pingreq_ip_entered} -c 3") # Pings it 3x.
            print("") # Adds a break in the lines
            break # Stops any loops.
    else :  ## MY CODE ##
        print('YOU MUST AGREE TO THE TERMS BEFORE USE!')
        sys.exit()

# Below here is under development and is best ignored for now!

# VulnCheck
#
#if args['vulncheck']:
#    logo.shepherd_logo()
#    print(notice)
#    yn = input()
#    if yn == 'y' or yn =='Y':
#        
#    else :
#        print('YOU MUST AGREE TO THE TERMS BEFORE USE!')
#        sys.exit()
#
#
# WhoIsRec

if args['whoisrec']:
    logo.shepherd_logo()
    print(notice)
    yn = input()
    if yn == 'y' or yn =='Y':
        while True:
            print("\n") # Adds a break in the lines
            pingreq_ip_entered = input("\nPlease enter the public ip address that you want to record grab: ") # Just asks you to give the program what IP you want to whois.
            print("\n") # Adds a break in the lines
            print(f"{pingreq_ip_entered} is the entered IP!") # Let's you know the IP was accepted for use.
            print("\n") # Adds a break in the lines
            break
            
        while True:
            os.system(f"whois {pingreq_ip_entered}") # whois request grabs.
            print("") # Adds a break in the lines
            break # Stops any loops.
    else :
        print('YOU MUST AGREE TO THE TERMS BEFORE USE!')
        sys.exit()

## CrypteX
#
#if args['cryptex']:
#    logo.shepherd_logo()
#    print(notice)
#    yn = input()
#    if yn == 'y' or yn =='Y':
#        
#    else :
#        print('YOU MUST AGREE TO THE TERMS BEFORE USE!')
#        sys.exit()
#
#
## Main Program
#
#if args['cli']:
#    logo.shepherd_logo()
#    print(notice)
#    yn = input()
#    if yn == 'y' or yn =='Y':
#        
#    else :
#        print('YOU MUST AGREE TO THE TERMS BEFORE USE!')
#        sys.exit()
#
#    if ch == 1:
#        q = input('SEARCH : ')
#        print('\n Performing PingReq Check\n')
#        search_url.url_search(q)
#
#
#    elif ch == 3:
#        s = input('SEARCH BOOKS/AUTHORS: ')
#        q = str('book:' + s)
#        print('\nSearching Books: \n')
#        search_url.url_search(q)
#
#
#    elif ch == 4:
#        s = input('SEARCH SONGS/ARTISTS: ')
#        q = str('?intitle:index.of?mp3 ' + s)
#        print('\nSearching Songs: \n')
#        search_url.url_search(q)
#
#
#    elif ch == 5:
#        info.information()
#
#
#    elif ch == 6:
#        hacking_menu()
#        if ch6 == 1:
#            wp.wordpress()
#
#        elif ch6 == 2:
#            q = str('filetype:ini “wordfence”')
#            print('\nSearching... \n')
#            search_url.url_search(q)
#
#        elif ch6 == 3:
#            up.userpass()
#
#        elif ch6 == 4:
#            cam.cameras()
#
#        elif ch6 == 5:
#            q = str('inurl:/proc/self/cwd')
#            print('\nSearching... \n')
#            search_url.url_search(q)
#
#        elif ch6 == 6:
#            q = str('allintext:username filetype:log')
#            print('\nSearching... \n')
#            search_url.url_search(q)
#
#        elif ch6 == 7:
#            ftp.ftp()
#
#        else:
#            print('INVALID OPTION : ')
#            sys.exit()
#
#
#
#    else:
#        print('INVALID OPTION! \n EXITING ')
#        sys.exit()