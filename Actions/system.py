import os
import datetime as dt
import shutil as sl
import subprocess as sp

from .other import SizeHelper

class System:

    def Time(self) -> None :
        print(dt.datetime.now())
    
    def DiskSpace(self,Path: str ='/') -> None: 
        total , used , free = sl.disk_usage(Path)
        print("Total :",SizeHelper(total))
        print("Used  :",SizeHelper(used))
        print("Free  :",SizeHelper(free))
    
    def CWD(self)->None:
        print(os.getcwd())

    def CD(self,Path: str) -> None:
        try:
            os.chdir(Path)
        except Exception as e:
            print(e)
    
    def LS(self,path: str='.') -> None:
        try:
            sp.run(['ls','.'])
        except Exception as e:
            print(e)


