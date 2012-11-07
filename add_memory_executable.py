#!/Library/Frameworks/Python.framework/Versions/3.2/bin/python3.2

## This program is an executable for adding keyword value pairs to the dictionary. It uses the value parsing method to parse value strings. It requires user approval to overwrite an existing keyword and to finalize the keyword, value pair to be added.


import sys
sys.path.append('/Users/kevin/Library/Jarvis/Jarvis_Memory')
from Jarvis_Memory_Dictionary import *
from Value_Objects_Jmemory import *

## Store the memory dictionary in the variable jm_dict
jm_dict = jmemory_dict.read()


## These while loops ensure that the use has added the memory they desire
continue_program = False
rerun = True
## the "rerun" loop ensures the user gets the keyword value pair they desire
while rerun == True:
    ## the "continue_program" loop ensures the user does not overwrite a keyword unless they want to
    while continue_program == False:
        keyword = input("keyword? ")
        ## checks if keyword already exists
        if keyword in jm_dict:
            print("That keyword is already used.")
            replace_test = input("Would your like to replace it? ")
            if replace_test == True or replace_test == "yes" or replace_test == "y" or replace_test == "Yes":
                continue_program = True
            else:
                continue_program = False
        else:
            continue_program = True

    value_string = input("value? ")
    new_value = value_info.string_to_value_info_parser(value_string)

    ## User approves key word value pair
    print("is this the keyword, value pair you wish to add?")
    print("[{}]: ".format(keyword),new_value)
    rerun_input = input("> ")   ## This line controlls the rerun loop. Program will start over on any answer other than the ones in the following if statement
    if rerun_input == True or rerun_input == "yes" or rerun_input == "y" or rerun_input == "Yes":
        jm_dict.add("{}".format(keyword),new_value)
        print("it was added")
        rerun = False
    else:
        continue_program = False




            
