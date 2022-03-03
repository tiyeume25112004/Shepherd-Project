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
import core.logo as logo # My logo, of course.
import core.colors as colors # We all love a splash of color.
import core.mods as mods # So we can let people modify it easier!

# Start of menu script caller.
def vulncheck():
    def vulncheck_menu():
        global ch
        mods.clear_screen()
        logo.shepherd_logo()

        print(f'''
    CHOOSE OPTION :
        {colors.bcolors.OKBLUE}[~]{colors.bcolors.ENDC} CrypteX         (Waiting)     [x]
        ''')

        ch = int(input("    --> "))
        print('\n\n')


    vulncheck_menu()


    if ch == 1:
        print('\n Running...\n')
        time.sleep(1)

    elif ch == 2:
        print('\n Running...\n')
        time.sleep(1)

    else:
        print('INVALID OPTION  \n TRY AGAIN')
        sys.exit()