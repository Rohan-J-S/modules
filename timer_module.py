import time
import threading

def timer():
    """ no input args retun value True when timer ends"""
    global ctdn
    ctdn = 31 #number of seconds
    while ctdn>0:
        ctdn -= 1
        time.sleep(1)
    return True 
  

