import shutil as sl
from pathlib import Path


from other import TerminalDimensions as TD

class Folder:

    def Create(self,FolderName: Path) -> None:
        if (FolderName.exists()):
            print(f"{FolderName.name} Aleady in {FolderName.resolve().parent.name}")
        else:
            try:
                FolderName.mkdir()
                print(f"{FolderName.name} Created Successfully")
            except:
                print("Error In Creating File")
    

    def Show(self,FolderName: Path='.') -> None:
        if (not FolderName.is_dir()):
            print(f"{FolderName.name} Is File")
            return
        Width = TD()
        name_width = max(Width//2,20)
        type_width = Width - name_width - 5
        print(f"{'NAME':<{name_width}}  {'TYPE':<{type_width}}")
        print("-"*Width)
        for items in FolderName.iterdir():
            Type: str = ("file" if (not items.is_dir()) else "folder")
            print(f"{str(items):<{name_width}}  {Type:<{type_width}}")

    def RShow(self,FolderName: Path='.') -> None:
        if (not FolderName.is_dir()):
            print(f"{FolderName.name} Is File")
            return
        Width = TD()
        name_width = max(Width//2,20)
        type_width = Width - name_width - 5
        print(f"{'NAME':<{name_width}}  {'TYPE':<{type_width}}")
        print("-"*Width)
        for items in FolderName.rglob("*"):
            Type: str = ("file" if (not items.is_dir()) else "folder")
            print(f"{str(items):<{name_width}}  {Type:<{type_width}}")

    def Move(self, FOlderName: Path, Destination: Path) -> None:
        if (FOlderName.exists() and Destination.is_dir()):
            try:
                sl.move(FOlderName,Destination)
                print(f"{FOlderName.name} Moved Successfully to {Destination.name}.")
            except Exception:
                print(f"Error Moving File")
        elif (not FOlderName.exists()):
            print(f"{FOlderName.name} Not Found.")
        elif (not Destination.exists()):
            print(f"{Destination.name} Not Found.")

    def Copy(self,Source:Path,Destination:Path) -> None:
        if (Source.is_dir() and Destination.is_dir()):
            try:
                des = Destination / Source.name
                sl.copytree(Source,des,dirs_exist_ok=True)
                print(f"{Source.name} Directory Copied Successfully to {Destination.resolve().name} Directory")
            except Exception as e:
                print('Error In Copying',e)
        elif (not Source.exists()):
            print(f"{Source.name} Directory Not Exists")
        elif (not Destination.exists()):
            print(f"{Destination.name} Directory Not Found")
        elif (not Destination.is_dir()):
            print(f"{Destination.name} Is FIle")

    def Rename(self, OldName: Path, NewName: Path) -> None:
        if (OldName.exists() and not NewName.exists()):
            try :         
                OldName.rename(NewName)
                print(f"Renamed Successfully {OldName.name} -> {NewName.name}")
            except Exception :
                print(f"Error In Renaming.")
        elif (not OldName.exists()):
            print(f"{OldName.name} Is Not Found.")
        elif (NewName.exists()):
            print(f"Error {NewName.name} Is Aleady in {NewName.resolve().parent.name} Directory.")

    def Delete(self,FolderName:Path) -> None:
        if (FolderName.exists()):
            try:
                sl.rmtree(FolderName)
                print(f"{FolderName.name} Deleted Successfully.")
            except Exception :
                print(f"Error In Deleting {FolderName.name}")
        else:
            print(f'{FolderName.name} Not Found.')
        


f = Folder()
a = Path('hellojdsidsa')
b = Path('hwll')
