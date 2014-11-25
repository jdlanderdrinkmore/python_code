#!/usr/bin/env python
#-*- coding=utf-8 -*-


def power(x,n=2):
	s = 1;
	while n > 0:
		n = n -1
		s *= x
	return s

p = raw_input("Please input two numbers,as the pattern a,b:\n")
n = p.split(',')
#print n
a = int(n[0])
b = int(n[1])
print 'The result of power(%d,%d) is %d' % (a,b,power(a,b))