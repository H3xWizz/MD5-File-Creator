import os
import os.path
import string
import sys
import hashlib
import glob

fname = sys.argv[1]
fnumber = 0

def get_md5():
    global hashcode
    hashcode = (hashlib.md5(fname.encode()).hexdigest())
    print("==========================================")
    print("File: " + str(fnumber))
    print("Name: " + fname)
    print("Hash: " + hashcode)
    print("==========================================")

def create_md5():
    hfile = open(fname + ".md5", "w")
    hfile.write(hashcode)
    hfile.close


print("Making MD5 for " + fname + "...")

for fname in glob.iglob(os.getcwd() + "/**/*" + fname, recursive = True):
    fnumber = fnumber + 1
    get_md5()
    create_md5()

print("==END==")