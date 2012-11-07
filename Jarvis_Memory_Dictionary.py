import pickle

## This is the dictionary containing the keys and values for Jarvis' Memory. It inherits all the functionality from regular python dicts and adds some functionality, shown in the function
class jmemory_dict(dict):
    
    def __init__(self,*arg,**kw):
        super(jmemory_dict, self).__init__(*arg, **kw)
    
    ## Reads the memory from the pickle doc
    def read():
        JMemory_File_Location = "/Users/kevin/Library/Jarvis/Jarvis_Memory/Jarvis_Memory.dat"
        JMemory_File = open(JMemory_File_Location,'rb')
        Memory_Dictionary = pickle.load(JMemory_File)
        JMemory_File.close()
        return(Memory_Dictionary)
    
    ## Writes a new dictionary to the pickle doc. Should only be used privately in this class
    def write_DO_NOT_USE(New_Dictionary):
        JMemory_File_Location = "/Users/kevin/Library/Jarvis/Jarvis_Memory/Jarvis_Memory.dat"
        JMemory_File = open(JMemory_File_Location,'wb')
        pickle.dump(New_Dictionary, JMemory_File)
        
        JMemory_File.close()

    ## Adds a new keyword and value pair to the dictionary. Note that it adds it to the dictionary currently used in the code and the one stored in the pickle doc, ensuring that they always match.
    def add(self,keyword,value):
        self[keyword] = value
        jmemory_dict.write_DO_NOT_USE(self)
        
    ## Removes keyword and value pair from the dictionary, given the keyword. Note that it removes it from the dictionary currently used in the code and the one stored in the pickle doc, ensuring that they always match.
    def remove(self,keyword):
        del self[keyword]
        jmemory_dict.write_DO_NOT_USE(self)

