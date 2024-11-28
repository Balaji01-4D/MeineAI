import os
import datetime as dt
import shutil as sl
from pathlib import Path
from time import ctime


from Actions import other
class System:

    def Time(self) -> None :
        print(dt.datetime.now())
    
    def DiskSpace(self, Destination: Path =Path('/')) -> None: 
        total , used , free = sl.disk_usage(Destination)
        print("Total :",other.SizeHelper(total))
        print("Used  :",other.SizeHelper(used))
        print("Free  :",other.SizeHelper(free))
    
    def GetCurrentDir(self) -> None:
        path:Path = Path('.')
        print(f"{path.resolve()}")


    def CD(self, Destination: Path) -> None:
        if (Destination.exists() and Destination.is_dir()):
            try:
                os.chdir(Path)
            except PermissionError:
                print(f"Permission Denied")            
            except Exception:
                print(f"Can't Change directory to {Destination.name}")
        elif (Destination.is_file()):
            print(f"Cant Change {Destination.name} Is File.")
        else:
            print(f"{Destination.name} Not Found.")
    def Info(self, Name : Path) -> None:
        if (not Name.exists()):
            print(f"{Name.name} Not Found")
            return
        size = other.SizeHelper(Name.stat().st_size) 
        stats = Name.stat()
        info : dict ={
            'Name' : Name.name,
            'Path' : str(Name.resolve()),
            'size' : size,
            'Type' : "File" if (not Name.is_dir()) else "Directory",
            'Created' : ctime(stats.st_ctime),
            'Last Modified' : ctime(stats.st_mtime),
            'Last Accessed' : ctime(stats.st_atime),
            'Mode' : stats.st_mode
        }
        for key,value in info.items():
            print(f"{key} : {value}")
            


