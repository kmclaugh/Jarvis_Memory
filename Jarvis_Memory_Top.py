print("Jarvis Memory Top\n")

import sys
sys.path.append('/Users/kevin/Library/Jarvis/Jarvis_Memory')
from Jarvis_Memory_Dictionary import *
from Value_Objects_Jmemory import *
import pickle


jm_dict = jmemory_dict.read()
print(jm_dict)
