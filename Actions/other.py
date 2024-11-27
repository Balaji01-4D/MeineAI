from pathlib import Path 
from time import ctime
import shutil as sl
def SizeHelper(Size : int) -> None:
    for unit in ['B','KB','MB','GB']:
        if (Size < 1024):
            return f"{Size:.2f} {unit}"
        Size/=1024

def Is_subsequence(Sub: str,Main: str) -> None:
    it=iter(Main)
    return all(item in it for item in Sub)


def Info(Name : Path) -> None:
    if (not Name.exists()):
        print(f"{Name.name} Not Found")
        return
    size = SizeHelper(Name.stat().st_size) 
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

def TerminalDimensions():
    return sl.get_terminal_size().columns
    
    