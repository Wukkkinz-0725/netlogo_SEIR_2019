#! /usr/bin/env python
import os
import git
import sys
import subprocess

oldrev,newrev,refname = sys.stdin.readline().strip().split(' ')
print('oldref:%s, newrev:%s, refname:%s'%(oldrev, newrev, refname))
