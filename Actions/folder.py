import os
import shutil as sl
import subprocess as sp

class Folder:

    def Create(self,FolderName: str) -> None:
        try:
            os.mkdir(FolderName)
            print("Folder Created Successfully")
        except Exception as e:
            print(e)

    def Show(self,FolderName: str=None) -> None:
        try:
            if (FolderName == None):
                FolderName = '.'
            print(os.listdir(FolderName))
        except Exception as e:
            print(e)

    def Move(self,FileName: str,Location: str) -> None:
        try:
            sl.move(FileName,Location)
            print("Folder Moved Successfully")
        except Exception as e:
            print(e)

    def Copy(self,Source: str,Destination: str) -> None:
        try:
            if ('/' in Destination):
                l=Source.split('/')
                Destination = os.path.join(Destination,l[len(l)-1])
            sl.copytree(Source,Destination)
            print("Folder Copied Successfully")
        except Exception as e:
            print(e)

    def Rename(self,OldName: str,NewName: str) -> None:
        try:      
            print(os.getcwd())
            os.rename(OldName,NewName)
            print(f"Folder Renamed Successfully")
        except Exception as e:
            print(e)

    def Delete(self,FolderName: str) -> None:
        try:
            sl.rmtree(FolderName)
            print(f"{FolderName} Deleted Successfully")
        except Exception as e:
            print(e)
        
    def FolderSize(self,FolderName: str='.') -> None:
        try:
            size=sp.run(['du','-sh',FolderName],text=True,capture_output=True)          #Linux Cmd
            print(size.stdout.strip())
        except Exception as e:
            print(f"ERROR:{e}")

