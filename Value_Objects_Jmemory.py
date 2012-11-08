#print("Value Object\n")

## Define the class, value_info, that will be used as the values in the memory dictonary. The value class is superclass of a dictionary with a more appropriate str method an easier create new value method, and a string to value parser

import sys
sys.path.append('/Users/kevin/Library/Jarvis/Jarvis_Memory')
from Find_Keywords_Jmemory import *

class value_info(dict):
    
    def __init__(self,*arg,**kw):
        super(value_info, self).__init__(*arg, **kw)

    def create_new_value(self,value_key,value_information):
        self["{}".format(value_key)]="{}".format(value_information)

    def __str__(self):
        output_string = ""
        for key in self:
            if key[0:4] == "info":
                value = self[key]
                temp_string = "{}, ".format(value)
                output_string += temp_string
            else:
                value = self[key]
                temp_string = "{} = {}, ".format(key,value)
                output_string += temp_string
        output_string = output_string[0:-2].replace("  "," ")
        return(output_string)

    def __repr__(self):
        output_string = ""
        for key in self:
            if key[0:4] == "info":
                value = self[key]
                temp_string = "{}, ".format(value)
                output_string += temp_string
            else:
                value = self[key]
                temp_string = "{} = {}, ".format(key,value)
                output_string += temp_string
        output_string = output_string[0:-2].replace("  "," ")
        return(output_string)

    ## Defines a method for parsing a string into a value_info instance. No error checking is done with this method so this must only be used when the provided string definetly contains a value to be parsed.
    def string_to_value_info_parser(value_string):
        items = value_string.split(",")
        this_value = value_info()
        counter = 1
        for item in items:
            if "=" in item:
                Encoding_Boole = check_for_keyword("encod",item)
                if Encoding_Boole == True:
                    parts = item.split("=")
                    type = parts[1]
                    this_value["encoding"] = type
                Category_Boole = check_for_keyword("categ",item)
                if Category_Boole == True:
                    parts = item.split("=")
                    type = parts[1]
                    this_value["category"] = type
                elif Encoding_Boole == False and Category_Boole ==False:
                    parts = item.split("=")
                    keyname = parts[0]
                    type = parts[1]
                    this_value["{}".format(keyname)] = type
                            
            else:
                keyname = "info{}".format(counter)
                this_value["{}".format(keyname)] = item
        return(this_value)


##Test bench for string to value parser
#teststring = "Routing Number = 111000025 (not encoded), Account Number = 1158-9470-2607, encoding = std numerical"
#test_value = value_info.string_to_value_info_parser(teststring)
#
#print(test_value)


