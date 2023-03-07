from os import listdir
from os.path import isfile, join
import os

userFile = "user.json"
class function():
    def __init__(self,mode):
        self.folder = None
        self.password = None
        self.thisdict = {}
        self.mode = mode
        self.folder = None

    def switch(self):

        if self.mode == "view":
            while(1):
                print("input inbox(choose inbox) or draft(for draft) or sent(for sent) or exit(for exit)")
                self.folder= input("which folder do you want to view:  ")
                if self.folder == "exit":
                    break
                else:
                    self.viewF()
        elif self.mode == "compose":
            Line = ""
            title = input("Please input email title: ")
            print("Please enter Email content (put '.' at the end when you want to finish")
            while (1):
                x = input()
                Line = Line + " " + x
                if "." in x:
                    break
            save = input("save(save the file) or sent(send the file)? ")
            if save == "save":
                dirSave = join("draft", "'" + title + "'")
                print("save dir", dirSave)
                command = "echo " + Line + ">>" + dirSave
                os.system(command)
            else:
                print("Your email has been sent")
                dirSave = join("sent", "'" + title + "'")
                command = "echo " + Line + ">>" + dirSave
                os.system(command)
        elif self.mode == "delete":
            while(1):
                self.folder = input(
                "which files do you want to delete. Please input inbox if inbox files or input draft if draft files or sent if sent files:  ")
                self.view()
                filenum = input("which file do you want to delete? or n(no): ")
                if filenum == "n":
                    break
                if filenum.isnumeric():
                    tmpName = str(self.onlyfileD[int(filenum)])
                    print("tmpName", tmpName)

                    command = "rm " + "'" + tmpName + "'"
                    os.system(command)
                    self.view()
                else:
                    print("please enter the index of the file")

        elif self.mode == "edit":
            while(1):
                self.folder = "draft"
                self.view()
                if filenum == "n":
                    break
                else:
                    filenum = input("which file do you want to edit? or n(no): ")
                    tmpName = str(self.onlyfileD[int(filenum)])
                    print("tmpName", tmpName)
                    command = "vim " + "'" + tmpName + "'"
                    os.system(command)
                    self.view()

    def view(self):
        self.onlyfiles = [f for f in listdir(self.folder ) if isfile(join(self.folder, f))]
        print("onlyfiles",self.onlyfiles)
        self.onlyfileD = [join(self.folder , f) for f in listdir(self.folder ) if isfile(join(self.folder, f))]
        count = 0
        print("Current Email in " + self.folder)
        for item in (self.onlyfiles):
            print(str(count) + " " + item)
            count = count + 1

    def viewF(self):
        while(1):
            self.view()
            filenum = input("which file do you want to see(enter index of file)? or n(no): ")

            if filenum == "n":
                break
            else:
                tmpName = str(self.onlyfileD[int(filenum)])
                if filenum.isnumeric():
                    print("***************File content********************")
                    command = "cat " + "'" + tmpName + "'"
                    os.system(command)
                    print("\n")
                    print("***************File content********************")
                else:
                    print("Please enter the index of the file")