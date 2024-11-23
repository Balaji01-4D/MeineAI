import os
import shutil as sl
import subprocess as sp

class File:

    def Move(self,FileName: str,Location: str) -> None:
        try:
            sl.move(FileName,Location)
            print("File Moved Successfully")
        except Exception as e:
            print(e)
    
    def Delete(self,FileName:str,Location:str='.') -> None:
        try:
            if (Location!= None):
                FileName = os.path.join(Location,FileName)
            os.remove(FileName)
            print("File Moved Successfully")
        except Exception as e:
            print("ERROR",e)

    def Rename(self,OldName:str,NewName:str) -> None:
        try:         
            os.rename(OldName,NewName)
            print("Rename Successfully")
        except Exception as e:
            print(e)
    
    def Copy(self,Source:str,Destination:str) -> None:
        '''
        it is used to copy the file 
        '''
        try:
            sl.copy(Source,Destination)
            print("Copied Successfully")
        except Exception as e:
            print(e)
    
    def CreateFile(self,Name:str,Location:str=".") -> None:
        Name = os.path.join(Location,Name)
        os.system("touch "+Name)                                # Linux command
        print("File Created Successfully")
    
    def ShowContent(self,FileName:str) -> None:
        try:
            with open(FileName,'r') as file:
                print(file.read())
        except Exception as e:
            print(e)

    def ClearContent(self,FileName:str) -> None:
        f=open(FileName,'w')
        print("Content Cleared !")



    def FileSize(self,FileName:str='.') -> None:
        try:
            size=sp.run(['du','-sh',FileName],text=True,capture_output=True)
            print(size.stdout)
        except Exception as e:
            print(e)
            