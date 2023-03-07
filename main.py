import user
import function

current_user = user.user()
current_user.getDict()
print("***********************************************")
print("Welcome to my Email Simulation")
print("Standard email operations include (but are not limited to) composing emails, saving & editing drafts, sending emails, viewing inbox or sentbox or drafts, and deleting emails.")
print("***********************************************")

while True:
    user_response = input("Do you have an account yet (y or n) ?")
    if user_response == "y":
        current_user.getDict()
        current_user.logIn()
        while True:
            function_mode = input("Please choose amongst functions: "+
                         " input one of these functions: compose(compose emails) "+
                         " view(view emails) "+
                         " delete(delete) "+
                          " n(log out): ")
            if function_mode == "n":
                break
            else:
                current_function = function.function(function_mode)
                current_function.switch()
    else:
        current_user.registration()
        current_user.saveFile()

