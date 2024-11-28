import time
a=time.time()
print(f'{a-0.0000:.2f}')
import re
import os
import spacy
from pathlib import Path


import Actions as op
import Actions.Myrequest as Req


nlp = spacy.load('en_core_web_sm')
b=time.time()

FILE = op.File()
DIR = op.Folder()
SEARCH = op.Search()
SYS = op.System()
ZIP = op.Zip

print(f"{b-a:.2f}")


def Cli():
    while True:
        Command: str = input(">>> ")
        b=time.time()
        try:
        
            if (re.fullmatch(r"[0-9+\-*/%(). ]+",Command)):
                print(eval(Command))

            elif bool(re.search(r"\b[sS]hell\b",Command)):
                sys:str = re.sub(r"\b[sS]hell\b","",Command)
                print("system command",sys)
                os.system(sys)

            else :
                doc = nlp(Command)
                Labels , Texts = [],[]
                for ent in doc.ents:
                    Labels.append(ent.label_)
                    Texts.append(ent.text)
                CDict = op.other.CMDMapper(Labels,Texts)
                Action:str = CDict['ACTION']
                Action = Action.lower()

                

                if (Action == "delete"):
                    Delete(Action,CDict)
                    
                elif (Action == "rename"):                 # RENAME
                    Rename(Action,CDict)

                elif(Action == 'copy'):                    # COPY
                    Copy(Action,CDict)
                
                elif(Action == 'move'): # COPY
                    Move(Action,CDict)
                
                elif (Action == 'create'):                        # CREATE
                    Create(Action,CDict)               
                
                elif (Action == 'clear'):                       # CLEAR CONTE
                    Clear_content(Action,CDict)
                
                elif (Action == 'show content'):                        # SHOW '
                    Show_content(Action,CDict)
                
                elif ('cd'  or 'change directory' in Action): 
                    Cd(Action,CDict) 

                elif (Action == 'cwd' or  'pwd'):      # CWD
                    print(os.getcwd())
                
                elif ('space'  or 'disk' in Action):    # DISK SPACE
                    Disk_space(CDict)

                elif (Action in 'time'):                        # TIME
                    SYS.Time()

                elif (Action == 'search text'):
                    Search_txt(Action,CDict)
            
                elif (Action == 'search file'):
                    Search_file(Action,CDict)

                elif (Action == 'search folder'):
                    Search_folder(Action,CDict)

                elif (Action == 'compress' or 'zip'):
                    Compress(Action,CDict)
                
                elif (Action == 'extract' or 'decompress'):
                    Extract(Action,CDict)
                
                elif (Action == 'info' or 'details'):
                    Info(CDict)
                


        
        except Exception as e:

            print("error: ",e)


def Info(CDict: dict):
    if (CDict.__contains__('FOLDER')):
        SYS.Info(CDict['FOLDER'])
    else :
        Req.GetName('Show Details')

def Extract(Action: str,CDict: dict):
    if (CDict.__contains__('FILE')):
        ZIP.Extract(Path(CDict['FILE']))
    elif (CDict.__contains__('FOLDER')):
        ZIP.Extract(Path(CDict['FOLDER']))
    else :
        Req.GetName(Action)

def Compress(Action: str, CDict: dict):
    if (CDict.__contains__('FILE')):
        ZIP.Compress(Path(CDict['FILE']))
    elif (CDict.__contains__('FOLDER')):
        ZIP.Compress(Path(CDict['FOLDER']))
    else :
        Req.GetName(Action)

def Clear_content(Action,CDict):      
    if (CDict.__contains__('FILE')):
        FileName = Path(CDict['FILE'])
        FILE.ClearContent(FileName)
    else :
        Req.GetFile(Action)

def Create(Action,CDict):
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

def Move(Action,CDict):
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

def Show_content(Action,CDict):
    if (CDict.__contains__('FILE')):
        FileName = Path(CDict['FILE'])
        FILE.ShowContent(FileName)
    else :
        Req.GetFile(Action)

def Copy(Action,CDict):
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
        
def Rename(Action,CDict):
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

def Delete(Action,CDict):
    if (CDict.__contains__('FILE')):
        Filename: Path = Path(CDict['FILE'])
        FILE.Delete(Filename)
    elif (CDict.__contains__('FOLDER')):
        FolderName: Path = Path(CDict['FOLDER'])
        DIR.Delete(FolderName)
    else :
        Req.GetName(Action)

def Cd(Action,CDict):
    if (CDict.__contains__('FOLDER')):
        FolderName = Path(CDict['FOLDER'])
        SYS.CD(FolderName)
    else:
        Req.GetDes(Action)

def Disk_space(CDict):
    if (CDict.__contains__('FOLDER')):
        SYS.DiskSpace(Path(CDict['FOLDER']))
    else :
        SYS.DiskSpace()

def Search_txt(Action,CDict):
    if (CDict.__contains__('TEXT')):
        Text = CDict['TEXT']
        if (CDict.__contains__('FOLDER')):
            SEARCH.TextFinderFile(Text,CDict['FOLDER'])
        else :
            SEARCH.TextFinderFile(Text)
    else:
        Req.GetTxt(Action)

def Search_file(Action: str, CDict: dict):
    if (CDict.__contains__('TEXT')):
        Text = CDict['TEXT']
        if (CDict.__contains__('FOLDER')):
            SEARCH.SearchFile(Text,CDict['FOLDER'])
        else :
            SEARCH.SearchFile(Text)
    else:
        Req.GetTxt(Action)

def Search_folder(Action: str , CDict: dict):
    if (CDict.__contains__('TEXT')):
        Text = CDict['TEXT']
        if(CDict.__contains__('FOLDER')):
            SEARCH.SearchFolder(Text,CDict['FOLDER'])
        else :
             SEARCH.SearchFolder(Text)
    else:
        Req.GetTxt(Action)
    


cd = time.time()

c = time.time()
print(f"{c-cd:.5f}")

