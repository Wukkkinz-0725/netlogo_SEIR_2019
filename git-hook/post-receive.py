#! /usr/bin/env python
import os
import git
import sys
import subprocess

def main():

	print('welcome to post-receive!')
	with open('/Users/jinze/Desktop/abc.txt', 'w') as output_file:
		output_file.write('abc') 
	sys.exit(0)

if __name__ == "__main__":
	main()