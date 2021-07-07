# Add the functions in this file

import sys
import json

def load_journal(f_name):
    f=open(f_name,)
    data=json.load(f)
    f.close()

    return data

