import numpy as np
import json
from os import path

userFile = "user.json"
class user:
    def __init__(self):
        self.username = None
        self.password = None
        self.thisdict = {}

    def registration(self):
        print("please register username and password")
        self.getUsername()

        self.thisdict[self.username] = self.password
        print("dictionary luuu",self.thisdict)
    def getUsername(self):
        print("***********************************************")
        self.username = input("User name: ")
        self.password = input("password: ")



    def getDict(self):
        if path.isfile(userFile):
            with open(userFile) as json_file:
                self.thisdict = json.load(json_file)
                print("Current account", self.thisdict)

    def logIn(self):
        tmp = 0
        while (1):
            wrongP = True
            if tmp != 0 & wrongP == True:
                print("wrong passwork and please type again")

            print("please input username and password")
            self.getUsername()
            if self.thisdict[self.username] == self.password:
                wrongP = False

                print("you are logging")

                print("***********************************************")
                break
            else:
                wrongP = True

            tmp = tmp + 1


    def saveFile(self):
        print("curent dictionary", self.thisdict)
        with open(userFile, 'w') as file:
            json.dump(self.thisdict, file)


