from sys import argv

import pip
from subprocess import call

requirements=["requests", "numpy", "Django", "pathlib",
                        "gunicorn==19.4.5", "Kotti==0.5.0a6", "markdown2==2.3.5", "moin==1.9.5",
                        "oauth2==1.5.153", "pycares==1.0.0", "pymongo==2.4.2", "PyYAML==3.11",
                        "qutebrowser==0.6.1", "recurly==2.6.0", "rsa==3.1.1", "topydo==0.13"]
def main():
    print ("Hello arguments: " + ', '.join(argv[1:]))
    
main()
