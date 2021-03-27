import numpy as np
import json
from os import path
import user
import function
from os.path import isfile, join
from os import listdir

usertmp = user.user()
usertmp.getDict()
import yaml
print("***********************************************")
print("Welcome to my Email Simulation")
print("OStandard email operations including (but not limited to) compose mail, save & edit draft, send email, view inbox or sentbox or drafts, delete email")
print("***********************************************")
while(1):

    yN = input("Do you have an account yet (y or n) ?")
    if yN == "y":
        usertmp.getDict()
        usertmp.logIn()
        while(1):

            mode = input("Please choose amongst functions: "+
                         " input one of these functions: compose(compose emails) "+
                         " view(view emails) "+
                         " delete(delete) "+
                          " n(log out): ")
            if mode == "n":
                break
            else:
                functiontmp = function.function(mode)
                functiontmp.switch()
    else:
        usertmp.registration()
        usertmp.saveFile()

