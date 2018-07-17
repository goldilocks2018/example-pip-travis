from sys import argv

import pip
from subprocess import call

requirements=[]
def main():
    try:
        for package in requirements:
            call("pip install " + package, shell=True)
    except Exception as e:
        print (e)
        pass
    print ("Hello arguments: " + ', '.join(argv[1:]))
