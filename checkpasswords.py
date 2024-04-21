#!/usr/bin/env python3
# -*- code: utf-8 -*-
##
## Filename:		checkpasswords.py
##
## Description:		check passwords sha1-hashes againts https://api.pwnedpasswords.com/range/
##

import logging
import requests
import hashlib
import argparse

##
## Create logger with handler
##

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
            '%(asctime)s : %(levelname)s : %(message)s',
            '%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
logger.addHandler(ch)

##====================================
##
## Parse arguments from commandline
##
##====================================
def parseArguments():

    parser = argparse.ArgumentParser(description='Check Passwords',
                                    usage='checkpasswords.py [-h] [OPTIONS]',
                                    epilog='Epilog: thanks for using my program!')

    ##
    ## Arguments
    ##

    parser.add_argument('-p','--password', action='store', type=str, default=False, 
        help='Plain text password [Default: %(default)s]')
    parser.add_argument('-f','--filename', action='store', nargs='*', default=False, 
        help='File with passwords [Default: %(default)s]')    
    parser.add_argument('-n','--nopad', action='store_false', default=False, 
        help='Remove padding [Default: %(default)s]')    
    parser.add_argument('-v','--verbose', action='store_true', default=False, 
        help='Verbose mode [Default: %(default)s]')

    ##
    ## Parse arguments
    ##

    options = parser.parse_args()

    ##
    ## Error checking
    ##
    if options.password==False and options.filename==False:
        logger.error("No password(s) in argument!")
        exit(0)

    return options

##===========================
##
## Read Passwords from file
##
##===========================
def readfromfile(files):
    passwords=[]
    for filename in files:
        try:
            with open(filename) as fp:
                for p in fp.readlines():
                    p=p.strip()
                    passwords.append(p)
        except Exception as orsak:
            logger.error(orsak)
            exit(0)
    return passwords

##===========================
##
## Hash passwords
##
##===========================
def hashpasswords(passwords):
    hashlist=[]

    for p in passwords:
        h=hashlib.sha1(p.encode('utf8')).hexdigest().upper()
        logger.debug("hash="+str(h))
        prefix=h[:6]
        suffix=h[6:]
        hashlist.append((h,p))
    return hashlist

##===========================
##
## Check Hashes
##
##===========================
def checkhashes(hashlist, nopad):
    
    for h,p in hashlist:
        pre=h[:5]
        suf=h[5:]
        if nopad:
            headers=""
        else:
            headers={"Add-Padding": "true"}
        res=requests.get('https://api.pwnedpasswords.com/range/'+str(pre), headers=headers)
        if res.status_code==200:
            logger.debug("range: "+str(pre)+" suffix: "+str(suf)+" pass: "+str(p))
            found=res.text.find(suf)
            if found>0:
                for f in res.text.split():
                    rtimes=f.split(':')[1]
                    rhash=f.split(':')[0]
                    if suf in f:
                        print("WARN: password found: <"+str(p)+"> times:", rtimes, "range:", pre,"api.hash:", rhash)
            if found<0:
                print("PASS: password NOT found in api.pwnedpasswords.com! Congratulations! Hash:", pre+suf)
            
##=======================
##
## Main
##
##=======================
if __name__ == '__main__':

    options=parseArguments()

    if options.verbose:
        logger.setLevel(logging.DEBUG)
        for handler in logger.handlers:
            if isinstance(handler, type(logging.StreamHandler())):
                handler.setLevel(logging.DEBUG)
                logger.debug('Debug logging enabled')

    ##
    ## Get Passwords from file
    ##
    passwords=[]
    if options.filename:
        passwords=readfromfile(options.filename)
    if options.password:
        passwords.append(options.password)
    ##
    ## Hash files
    ##
    hashes=hashpasswords(passwords)
    ##
    ## Check hashes
    ##
    if len(hashes)!=0:
        checkhashes(hashes, options.nopad)
    else:
        logger.error("No hashes to check for!")

##
## This file has not been truncated
##
