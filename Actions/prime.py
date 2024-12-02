import Actions as op
import Actions.Myrequest as Req
import os
from pathlib import Path
FILE = op.File()
DIR = op.Folder()
SEARCH = op.Search()
SYS = op.System()
ZIP = op.Zip


def WHatAction(Action: str, CDict: dict[str]) -> None:
    print(Action)
    if (Action in {'delete','rm','remove','pop','rmdir'}):
        
        Delete(Action,CDict)
        
    elif (Action in {"rename",'rn'}):                 # RENAME
        Rename(Action,CDict)

    elif(Action in {'copy','c','cp'} ):     
        Copy(Action,CDict)

    elif(Action in {'move','mv','push'}): # COPY
        Move(Action,CDict)

    elif (Action in {'create','make','mk'} ):                        # CREATE
        Create(Action,CDict)               

    elif (Action in {'clear content','clr','clear'}  ):                       # CLEAR CONTE
        Clear_content(Action,CDict)

    elif (Action == 'show content'):                        # SHOW '
        Show_content(Action,CDict)

    elif (Action in {'cd','change directory','go'}): 
        Cd(Action,CDict) 

    elif (Action in {'where','cwd','pwd','ls'}):      # CWD
        print(os.getcwd())

    elif (Action in {'space','disk'} ):    # DISK SPACE
        Disk_space(CDict)

    elif (Action == 'time'):                        # TIME
        SYS.Time()

    elif (Action == 'search text'):
        Search_txt(Action,CDict)

    elif (Action == 'search file'):
        Search_file(Action,CDict)

    elif (Action == 'search folder'):
        Search_folder(Action,CDict)

    elif (Action in {'z','compress','zip'}):
        Compress(Action,CDict)

    elif (Action in {'extract','decompress','uz'}):
        Extract(Action,CDict)

    elif (Action == {'info','details'} and CDict.__contains__('FILE') or CDict.__contains__('FOLDER')):
        Info(CDict)
    
    elif (Action == 'ip'):
        SYS.IP()
    
    elif (Action in {'my ram','ram'}):
        SYS.RAMInfo()
    elif (Action in {'system','sys'}):
        SYS.SYSTEM()
    elif (Action in {'battery','charge','bt'}):
        SYS.Battery()
    elif(Action in {'user','me'}):
        SYS.USER()
    elif (Action in {'disk','storage'}):
        SYS.DiskInfo()
    elif (Action in {'cpu'}):
        SYS.CPU()
    elif (Action in {'env','envirnoment variable'}):
        SYS.ENV()
    elif (Action in {'network','network info'}):
        SYS.NetWork()
    elif (Action in {'home directory','home'}):
        SYS.HomeDir()       



def Info(CDict: dict) -> None:
    if (CDict.__contains__('FOLDER')):
        SYS.Info(CDict['FOLDER'])
    else :
        Req.GetName('Show Details')

def Extract(Action: str,CDict: dict) -> None:
    if (CDict.__contains__('FILE')):
        ZIP.Extract(Path(CDict['FILE']))
    elif (CDict.__contains__('FOLDER')):
        ZIP.Extract(Path(CDict['FOLDER']))
    else :
        Req.GetName(Action)

def Compress(Action: str, CDict: dict) -> None:
    if (CDict.__contains__('FILE')):
        ZIP.Compress(Path(CDict['FILE']))
    elif (CDict.__contains__('FOLDER')):
        ZIP.Compress(Path(CDict['FOLDER']))
    else :
        Req.GetName(Action)

def Clear_content(Action: str,CDict: dict[str]) -> None:      
    if (CDict.__contains__('FILE')):
        FileName = Path(CDict['FILE'])
        FILE.ClearContent(FileName)
    else :
        Req.GetFile(Action)

def Create(Action: str,CDict: dict[str]) -> None:
    if (CDict.__contains__('FILE')):
        FileName: Path = Path(CDict['FILE'])
        if (CDict.__contains__('FOLDER')):
            FILE.MakeFile(Path,CDict['FOLDER'])
        else:
            FILE.MakeFile(Path)
    elif (CDict.__contains__('FOLDER')):
        FolderName: Path = Path(CDict['FOLDER'])
        if (CDict.__contains__('DESTINATION')):
            Des: Path = Path(CDict['DESTINATION'])
            DIR.Create(FolderName,Des)
        else:
            DIR.Create(FolderName)
    else :
        Req.GetName(Action)

def Move(Action: str,CDict: dict[str]) -> None:
    if (CDict.__contains__('FILE')):
        FileName: Path = Path(CDict['FILE'])
        if (CDict.__contains__('FOLDER')):
            Des: Path = Path(CDict['FOLDER'])
            FILE.Move(FileName,Des)
        else:
            Req.GetDes(Action)
    elif (CDict.__contains__('FOLDER')):
        FolderName: Path = Path(CDict['FOLDER'])
        if (CDict.__contains__('DESTINATION')):
            Des: Path = Path(CDict['DESTINATION'])
            DIR.Move(FolderName,Des)
        else:
            Req.GetDes(Action)
    else :
        Req.GetName(Action)

def Show_content(Action: str,CDict: dict[str]) -> None:
    if (CDict.__contains__('FILE')):
        FileName = Path(CDict['FILE'])
        FILE.ShowContent(FileName)
    else :
        Req.GetFile(Action)

def Copy(Action: str,CDict: dict[str]) -> None:
    if (CDict.__contains__('FILE')):
        FileName: Path = Path(CDict['FILE'])
        if (CDict.__contains__('FOLDER')):
            Des: Path = Path(CDict['FOLDER'])
            FILE.Copy(FileName,Des)
        else:
            Req.GetDes  (Action)
    elif (CDict.__contains__('FOLDER')):
        FolderName: Path = Path(CDict['FOLDER'])
        if (CDict.__contains__('DESTINATION')):
            Des: Path = Path(CDict['DESTINATION'])
            FILE.Copy(FolderName,Des)
        else:
            Req.GetDes(Action)
    else :
        Req.GetName(Action)
        
def Rename(Action: str,CDict: dict[str]) -> None:
    if (CDict.__contains__('FILE')):
        FileName: Path = Path(CDict['FILE'])
        if (CDict.__contains__('NEWNAME')):
            Des: Path = Path(CDict['NEWNAME'])
            FILE.Rename(FileName,Des)
        else:
            Req.GetNewName(Action)
    elif (CDict.__contains__('FOLDER')):
        FolderName: Path = Path(CDict['FOLDER'])
        if (CDict.__contains__('NEWNAME')):
            Des: Path = Path(CDict['NEWNAME'])
            DIR.Rename(FolderName,Des)
        else:
            Req.GetNewName(Action)
    else :
        Req.GetName(Action)

def Delete(Action: str,CDict: dict[str]) -> None:
    if (CDict.__contains__('FILE')):
        Filename: Path = Path(CDict['FILE'])
        FILE.Delete(Filename)
    elif (CDict.__contains__('FOLDER')):
        FolderName: Path = Path(CDict['FOLDER'])
        DIR.Delete(FolderName)
    else :
        Req.GetName(Action)

def Cd(Action: str,CDict: dict[str]) -> None:
    if (CDict.__contains__('FOLDER')):
        FolderName = Path(CDict['FOLDER'])
        SYS.CD(FolderName)
    else:
        Req.GetDes(Action)

def Disk_space(CDict) -> None:
    if (CDict.__contains__('FOLDER')):
        SYS.DiskSpace(Path(CDict['FOLDER']))
    else :
        SYS.DiskSpace()

def Search_txt(Action: str,CDict: dict[str]) -> None:
    if (CDict.__contains__('TEXT')):
        Text = CDict['TEXT']
        if (CDict.__contains__('FOLDER')):
            SEARCH.TextFinderFile(Text,CDict['FOLDER'])
        else :
            SEARCH.TextFinderFile(Text)
    else:
        Req.GetTxt(Action)

def Search_file(Action: str, CDict: dict) -> None:
    if (CDict.__contains__('TEXT')):
        Text = CDict['TEXT']
        if (CDict.__contains__('FOLDER')):
            SEARCH.SearchFile(Text,CDict['FOLDER'])
        else :
            SEARCH.SearchFile(Text)
    else:
        Req.GetTxt(Action)

def Search_folder(Action: str , CDict: dict) -> None:
    if (CDict.__contains__('TEXT')):
        Text = CDict['TEXT']
        if(CDict.__contains__('FOLDER')):
            SEARCH.SearchFolder(Text,CDict['FOLDER'])
        else :
             SEARCH.SearchFolder(Text)
    else:
        Req.GetTxt(Action)