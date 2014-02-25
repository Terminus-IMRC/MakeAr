#!/usr/bin/env python3
import sys

allar=[]
cursum=0

def func(level):
	global X, ar, cursum

	if level==X:
		if cursum==X*(X**2+1)/2:
			allar.append(ar[:])
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

def output_as_header():
	print("#ifndef AR_INSIDE")
	print("#define AR_INSIDE")
	print("#ifndef X")
	print("#error Define X in compile")
	print("#else")
	print("#if X!=%d"%X)
	print("#error X must be %d"%X)
	print("#endif")
	print("#endif")
	print()
	print("#define AR_LEN %d"%len(allar))
	print("AR_TYPE ar[AR_LEN][X]={")
	for i in range(len(allar)-1):
		print("\t{", end='')
		for j in range(X-1):
			print("%d,"%allar[i][j], end='\t')
		print("%d},"%allar[i][X-1])
	print("\t{", end='')
	for j in range(X-1):
		print("%d,"%allar[len(allar)-1][j], end='\t')
	print("%d}"%allar[len(allar)-1][X-1])
	print("};")
	print("#endif /* AR_INSIDE */")

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

	output_as_header()

def error(str):
	print("error: "+str)
	print("Usage: "+sys.argv[0]+" [X]")
	exit(1)

if __name__=='__main__':
	main()
