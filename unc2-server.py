#!/usr/bin/env python3

import sys
import os
import requests

def connections():
	print("This is the CONNECTIONS module")
	empty = input("Press ENTER")
	main_menu()

def module_2():
	print("This is MODULE2")
	empty = input("Press ENTER")
	main_menu()

def module_3():
	print("This is MODULE3")
	empty = input("Press ENTER")
	main_menu()


def main_menu():
	os.system('clear')
	print(
	'''
	███╗   ██╗███████╗███████╗██████╗ ██╗     ███████╗███████╗███████╗     ██████╗██████╗ 
	████╗  ██║██╔════╝██╔════╝██╔══██╗██║     ██╔════╝██╔════╝██╔════╝    ██╔════╝╚════██╗
	██╔██╗ ██║█████╗  █████╗  ██║  ██║██║     █████╗  ███████╗███████╗    ██║      █████╔╝
	██║╚██╗██║██╔══╝  ██╔══╝  ██║  ██║██║     ██╔══╝  ╚════██║╚════██║    ██║     ██╔═══╝ 
	██║ ╚████║███████╗███████╗██████╔╝███████╗███████╗███████║███████║    ╚██████╗███████╗
	╚═╝  ╚═══╝╚══════╝╚══════╝╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝     ╚═════╝╚══════╝
	'''
	)

	print(
	'''
	1) Connections from agents
	2) Something else
	3) One more thing
	4) Exit
	'''
	)

	choice = input("	N-C2~> ")

	if choice == "1" :
		connections()
	elif choice == "2" :
		module_2()
	elif choice == "3" :
		module_3()
	elif choice == "4" :
		exit()
	else:
		print("¯\_(ツ)_/¯ Try again!")
		main_menu()

main_menu()

