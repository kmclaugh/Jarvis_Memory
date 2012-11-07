#print("Find Key Words\n")

import re

teststring = "tell me test remember as test"


#converts a regex object or regex.findall list to a Boolean.
def regex_to_boole(regex_ouput):
    if type(regex_ouput) == list:
        if regex_ouput == []:
            return(False)
        else:
            return(True)
    else:
        if regex_ouput == None:
            return(False)
        else:
            return(True)

#uses a regex to check if a keyword is in a string, ignoring case. Returns a Boolean
def check_for_keyword(keyword, string):
    remember_finder = re.compile(keyword,re.IGNORECASE)
    remember_regex_match = remember_finder.findall(string)
    remember_boole = regex_to_boole(remember_regex_match)
    return(remember_boole)


