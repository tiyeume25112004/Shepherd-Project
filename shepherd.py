#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports.
import sys # System.
import os # Operating System functions.
import argparse # Google said I needed this.
import core.shepherd_logo as logo # My logo, of course.
import core.colors as colors # We all love a splash of color.
import core.mods as mods # So we can let people modify it easier!

# List of commands.
parser = argparse.ArgumentParser()
ap = parser.add_mutually_exclusive_group()
ap.add_argument('--cli', help='Run the Command Line version.\n', action='store_true') # Developing.
ap.add_argument('--pingreq', help='Send a customised ping.\n', action='store_true') # Working.
ap.add_argument('--vulncheck', help='Scan for Log4j, heartbleed, and a port-scanner!\n', action='store_true') # Developing.
ap.add_argument('--whoisrec', help='Domains lookup, nameservers, etc.\n', action='store_true') # Further research needed.
ap.add_argument('--cryptex', help='Utilise the CrypteX package developed by Cythes @ https://github.com/AlexKollar!\n', action='store_true') # Awaiting Alex.
ap.add_argument('--p-vpn', help='Utilise ProtonVPN through the P-VPN feed option.\n', action="store_true") # Further research needed.
ap.add_argument('-v', '--version', help='Version, nothing more or less.\n', action="version", version='2.2.5') # Working.
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
    mods.clear_screen() # Clears the screen.
    logo.shepherd_logo() # Prints the logo.
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


# PingReq.
if args['pingreq']:
    mods.clear_screen() # Clears the screen.
    print(notice) # Prints the notice seen above, again, if the screen was cleared.
    while True:
        print("\n") # Adds a break in the lines.
        pingreq_ip_entered = input("\nPlease enter the ip address that you want to ping: ") # Just asks you to give the program what IP you want to ping.
        print("\n") # Adds a break in the lines.
        print(f"IP/Domain: {pingreq_ip_entered}, is about to be pinged!") # Let's you know the IP was accepted for use.
        print("\n") # Adds a break in the lines.
        break

    while True:
        os.system(f"ping {pingreq_ip_entered} -c 3") # Pings it 3x.
        print("") # Adds a break in the lines.
        break # Stops any loops.
    else :  ## MY CODE ##
        exit()


# VulnCheck.
#if args['vulncheck']:
#   mods.clear_screen() # Clears the screen.
#   print(notice) # Prints the notice seen above, again, if the screen was cleared.
#    else :
#        exit()


# WhoIsRec.
if args['whoisrec']:
    mods.clear_screen() # Clears the screen.
    print(notice) # Prints the notice seen above, again, if the screen was cleared.
    while True:
        print("\n") # Adds a break in the lines.
        whoisrec_ip_entered = input("\nPlease enter the ip address that you want to record grab: ") # Just asks you to give the program what IP you want to whois.
        print("\n") # Adds a break in the lines.
        print(f"IP/Domain: {whoisrec_ip_entered}, locking on!") # Let's you know the IP was accepted for use.
        print("\n") # Adds a break in the lines.
        print("\n") # Adds a break in the lines.
        os.system(f"traceroute {whoisrec_ip_entered}") # trace routes the IP
        print("\n") # Adds a break in the lines.
        os.system(f"whois {whoisrec_ip_entered} -H") # whois request grabs.
        print("") # Adds a break in the lines.
        break # Stops any loops.
    else :
        exit()


# CrypteX.
if args['cryptex']:
    mods.clear_screen() # Clears the screen.
    print(notice) # Prints the notice seen above, again, if the screen was cleared.      
    while True:
        os.system("python3 ./modules/cryptex/cryptex.py") # Loads cryptex menu.
    else :
        exit()

# Main Program (Command Line).
#if args['cli']:
#    mods.clear_screen()
#    print(notice)
#    yn = input()
#    if yn == 'y' or yn =='Y':
#        
#    else :
#        print('YOU MUST AGREE TO THE TERMS BEFORE USE!')
#        exit()
#
#    if ch == 1:
#        q = input('SEARCH : ')
#        print('\n Performing PingReq Check\n')
#        search_url.url_search(q)
#
#
#    elif ch == 2:
#        s = input('SEARCH BOOKS/AUTHORS: ')
#        q = str('book:' + s)
#        print('\nSearching Books: \n')
#        search_url.url_search(q)
#
#
#    elif ch == 3:
#        s = input('SEARCH SONGS/ARTISTS: ')
#        q = str('?intitle:index.of?mp3 ' + s)
#        print('\nSearching Songs: \n')
#        search_url.url_search(q)
#
#
#    elif ch == 4:
#        info.information()
#
#
#    elif ch == 5:
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
#            exit()
#
#    else:
#        print('INVALID OPTION! \n EXITING ')
#        exit()