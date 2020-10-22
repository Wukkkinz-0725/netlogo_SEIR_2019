#! /usr/bin/python

import sys
import subprocess

def main():
	cmd = 'git diff --name-only --cached'
	result = subprocess.check_output(cmd, shell=True)
	files = result.split('\n')
	print('aaaa')
	print(files)

	# for file in files:
	# 	if file.endswith('py'):
	# 		print(file)
	# 		with open(file, 'r') as read_file:
	# 			tmp = read_file.read()
	# 			print(tmp)
	# print('AAAAAAAAA: %d', len(sys.argv))
	# print('BBBBBBBBB: %s' % str(sys.argv))
	# print('CCCCCCCCD')
	sys.exit(0)

if __name__ == "__main__":
	main()