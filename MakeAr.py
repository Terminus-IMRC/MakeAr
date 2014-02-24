#!/usr/bin/env python3
import sys

cursum=0

def func(level):
	global X, ar, cursum

	if level==X:
		if cursum==X*(X**2+1)/2:
			print(ar)
		return

	if level==0:
		start=1
	else:
		start=ar[level-1]+1

	for i in range(start, X**2+1):
		ar[level]=i
		cursum+=i
		if cursum<=X*(X**2+1)/2:
			func(level+1)
		cursum-=i

def main():
	global X, ar

	if len(sys.argv)!=2:
		error("specify X")

	try:
		X=int(sys.argv[1])
	except ValueError:
		error("the value is unrecognized")

	ar=[[]for x in range(X)]

	func(0)

def error(str):
	print("error: "+str)
	print("Usage: "+sys.argv[0]+" [X]")
	exit(1)

if __name__=='__main__':
	main()
