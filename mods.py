#!/usr/bin/python
# -*- coding: utf-8 -*-

# IMPORTS.
from os import system, name

# MAIN SCRIPT.
def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
