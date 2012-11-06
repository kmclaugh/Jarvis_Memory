print("Find Key Words\n")

import re

teststring = "tell me test remember as test"


#converts a regex object or regex.findall list to a Boolean.
def regex_to_boole(regex_ouput):
    if type(regex_ouput) == list:
        if listy == []:
            return(False)
        else:
            return(True)
    else:
        if regex_ouput == None:
            return(False)
        else:
            return(True)

#uses a regex to check for keyword "Remember." Returns a Boolean
def check_for_remember(string):
    remember_finder = re.compile("remem",re.IGNORECASE)
    remember_regex_match = remember_finder.match(string)
    remember_boole = regex_to_boole(remember_regex_match)
    return(remember_boole)

#test = check_for_remember(teststring)
#print(test)


#uses a regex to check for keyword "Tell me." Returns a Boolean
def check_for_tell_me(string):
    tell_me_finder = re.compile("tell me", re.IGNORECASE)
    tell_me_match = tell_me_finder.match(string)
    tell_me_boole = regex_to_boole(tell_me_match)
    return(tell_me_boole)

#test2 = check_for_tell_me(teststring)
#print(test2)

