import os
import shutil as sl
from subprocess import run
import pathlib as path
from pathlib import Path

class Folder:

    def Create(self,FolderName: str) -> None:
        try:
            os.mkdir(FolderName)
            print("Folder Created Successfully")
        except Exception as e:
            print(e)

    def Show(self,FolderName: str='.') -> None:
        try:
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

    def Delete(self,FolderName: Path) -> None:
        try:
            sl.rmtree(FolderName)
            print(f"{FolderName.name} Deleted Successfully")
        except Exception as e:
            print(e)
        
    def FolderSize(self,FolderName: str='.') -> None:
        try:
            size=run(['du','-sh',FolderName],text=True,capture_output=True)          #Linux Cmd
            print(size.stdout.strip())
        except Exception as e:
            print(f"ERROR:{e}")

