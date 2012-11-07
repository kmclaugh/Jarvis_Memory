#print("Value Object\n")

## Define the class, value_info, that will be used as the values in the memory dictonary. The value class will contain one info attribute, a category attribute, which defaults to None, and an encoding attribute, which also defaults to None
import sys
sys.path.append('/Users/kevin/Library/Jarvis/Jarvis_Memory')
from Find_Keywords_Jmemory import *

class value_info():
    def __init__(self,encode=None, category=None, information = None):
        self.encoding= encode
        self.category = category
        self.info = information
    
    ## Defines the print method for listing all attributes of the value_info instance, excluding predefined attributes that are set to defaults. Output string is just a formatting method.
    def __str__(self):
        output_string = ""
        for attr, value in vars(self).items():
            if attr != "encoding" and attr != "category":
                output_string = output_string + "{}, ".format(value)
        for attr, value in vars(self).items():
            if attr == "encoding" and value != None:
                output_string = output_string + "{} = {}, ".format(attr,value)
            elif attr == "category" and value != None:
                output_string = output_string + "{} = {}, ".format(attr,value)
        output_string = output_string[0:-2]
        return output_string

    def __repr__(self):
        output_string = ""
        for attr, value in vars(self).items():
            if attr != "encoding" and attr != "category":
                output_string = output_string + "{}, ".format(value)
        for attr, value in vars(self).items():
            if attr == "encoding" and value != None:
                output_string = output_string + "{} = {}, ".format(attr,value)
            elif attr == "category" and value != None:
                output_string = output_string + "{} = {}, ".format(attr,value)
        output_string = output_string[0:-2]
        return output_string
    
    ## Defines a method for parsing a string into a value_info instance. No error checking is done with this method so this must only be used when the provided string definetly contains a value to be parsed.
    def string_to_value_info_parser(value_string):
        items = value_string.split(",")
        this_value = value_info()
        
        for item in items:
            
            if "=" in item:
                
                Encoding_Boole = check_for_keyword("encod",item)
                if Encoding_Boole == True:
                    parts = item.split("=")
                    type = parts[1]
                    this_value.encoding = type
                Category_Boole = check_for_keyword("categ",item)
                if Category_Boole == True:
                    parts = item.split("=")
                    type = parts[1]
                    this_value.category = type
            else:
                this_value.info = item.replace(",","")
        return(this_value)


##Test bench for string to value parser
#teststring = "encoding = std num, 54321"
#test_value = value_info.string_to_value_info_parser(teststring)
#print(test_value)

