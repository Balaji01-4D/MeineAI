import os
import shutil as sl
import subprocess as sp
from pathlib import Path

class File:

    def Move(self,FileName: str,Location: str) -> None:
        try:
            sl.move(FileName,Location)
            print("File Moved Successfully")
        except Exception as e:
            print(e)
    
    def Delete(self,FileName:Path) -> None:
        try:
            FileName.unlink()
            print(f"{FileName.name} Moved Successfully")
        except (FileNotFoundError,FileExistsError) :
            print(f"{FileName.name} Not In Directory")
        except Exception as e:
            print("ERROR",e)

    def Rename(self,OldName:Path,NewName:Path) -> None:
        try:         
            os.rename(OldName,NewName)
            print("Renamed Successfully")
        except Exception as e:
            print(e)
    
    def Copy(self,Source:Path,Destination:Path) -> None:
        '''
        it is used to copy the file 
        '''
        try:
            sl.copy(Source,Destination)
            print("Copied Successfully")
        except Exception as e:
            print(e)
    
    def CreateFile(self,Name:Path,Location:str=".") -> None:
        Name = os.path.join(Location,Name)
        os.system("touch "+Name)                                # Linux command
        print("File Created Successfully")
    
    def ShowContent(self,FileName:Path) -> None:
        try:
            with open(FileName,'r') as file:
                print(file.read())
        except Exception as e:
            print(e)

    def ClearContent(self,FileName:Path) -> None:
        f=open(FileName,'w')
        f.close()
        print(f"{FileName.name} Content is Cleared")



    def FileSize(self,FileName:Path='.') -> None:
        try:
            size=sp.run(['du','-sh',FileName],text=True,capture_output=True)
            print(size.stdout)
        except Exception as e:
            print(e)
            