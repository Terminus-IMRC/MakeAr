#!/usr/bin/env python3
import sys

def func(level):
	global X

	print(X, level)

def main():
	global X

	if len(sys.argv)!=2:
		error("specify X")

	try:
		X=int(sys.argv[1])
	except ValueError:
		error("the value is unrecognized")

	func(0)

def error(str):
	print("error: "+str)
	print("Usage: "+sys.argv[0]+" [X]")
	exit(1)

if __name__=='__main__':
	main()
