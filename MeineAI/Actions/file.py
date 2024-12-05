import shutil as sl
from pathlib import Path



class File:

    def Move(self, FileName: Path, Destination: Path) -> None:
        FinalDestination = Destination / Path(FileName.name)
        if (FinalDestination.exists()):
            print(f"{Destination.name} Directory Has Already {FileName.name}")
            return
        if (FileName.exists() and Destination.is_dir()):
            try:
                sl.move(FileName,Destination)
                print(f"{FileName.name} Moved Successfully to {Destination.name}.")
            except Exception:
                print(f"Error Moving File")
        elif (not FileName.exists()):
            print(f"{FileName.name} Not Found.")
        elif (not Destination.exists()):
            print(f"{Destination.name} Not Found.")
    
    def Delete(self,FileName:Path) -> None:
        if (FileName.exists()):
            try:
                FileName.chmod(744)
                FileName.unlink()
                print(f"{FileName.name} Deleted Successfully.")
            except Exception :
                print(f"Error In Deleting {FileName.name}")
        else:
            print(f'{FileName.name} Not Found.')
        

    def Rename(self, OldName: Path, NewName: Path) -> None:
        if (OldName.exists() and not NewName.exists() and not OldName.is_dir()):
            try :
                if NewName.suffix == "":
                    NewName = NewName.with_suffix(OldName.suffix)                         
                OldName.rename(NewName)
                print(f"Renamed Successfully {OldName.name} -> {NewName.name}")
            except PermissionError:
                print(f"Permission Denied")
            except Exception :
                print(f"Error In Renaming.")
        elif (not OldName.exists()):
            print(f"{OldName.name} Is Not Found.")
        elif (NewName.exists()):
            print(f"Error {NewName.name} Is Aleady in {NewName.resolve().parent.name} Directory.")
    
    def Copy(self,Source:Path,Destination:Path) -> None:
        if (Source.exists() and Destination.is_dir()):
            try:
                sl.copy(Source,Destination)
                print("Copied Successfully")
            except PermissionError:
                print(f"Permission Denied")
            except Exception:
                print('Error In Copying')
        elif (not Source.exists()):
            print(f"{Source.name} Not Exists")
        elif (not Destination.is_dir()):
            print(f"{Destination.name} Not Found")
    
    def MakeFile(self,Name:Path,Destination:Path=Path(".")) -> None:
        Name = Destination / Name
        if (not Name.exists()):
            Name.touch()
            print(f"{Name.name} Is Created in {Destination.resolve().name} Directory")
        else:
            print(f"{Name.name} Is Already in {Destination.resolve().name} Directory")
    
    def ShowContent(self,FileName:Path) -> None:
        if (FileName.exists() and not FileName.is_dir()):
            try:
                with FileName.open() as file:
                    print(file.read())
                    print("End Of The FIle".center(21,"-"))
            except PermissionError:
                print(f"Permission Denied")
            except Exception :
                print(f"Error In Reading The {FileName.name}")
        elif (FileName.exists() and FileName.is_dir()):
            print(f"{FileName.resolve().name} Is Directory")
        elif (not FileName.exists()):
            print(f"{FileName.name} Not Found")

    def ClearContent(self,FileName:Path) -> None:
        try:
            if (FileName.exists() and not FileName.is_dir()):
                f=open(FileName,'w')
                f.close()
                print(f"{FileName.name} Content is Cleared")
            elif (FileName.is_dir() and FileName.exists()):
                print(f"{FileName.resolve().name} Is Directory")
            elif (not FileName.exists()):
                print(f"{FileName.name} Not Found")
        except PermissionError:
             print(f"Permission Denied")
        


