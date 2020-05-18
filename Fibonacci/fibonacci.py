#!/usr/bin/env python3

def Fib(N):
	x, y = 0, 1 #initialize the variables
	while (y < N):
		print(y, end = ' ', flush =True)
		x, y = y, x+y

N = int(input("Enter the number for which you need fibonacci series: "))

print(" The Fibonacci series for {} is : ". format(N))

Fib(N)