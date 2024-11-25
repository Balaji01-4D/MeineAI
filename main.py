import time
a=time.time()
print(f'{a-0.0000:.2f}')
import re
import os
import spacy
import pathlib as Path


import Actions as op
nlp = spacy.load('./MeineAI/summaMeineAI')
b=time.time()

File = op.File()
Dir = op.Folder()
search = op.Search()
Sys = op.System()

print(f"{b-a:.2f}")

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
            CDict: dict = {'FIle_FolderName':'.','Destination':'.'}
            print(f"Input Text: {Command}")
            print("Entities Detected:")
            for ent in doc.ents:
                print(f" - {ent.text} ({ent.label_})")
                CDict[ent.label_] = ent.text

            Action:str = CDict['Action']


            Source = Path.Path(CDict['FIle_FolderName'])
            

            if (Action.lower() == "delete"):                    # DELETE
                if Source.is_file():
                    File.Delete(Source)
                
                else :
                   Dir.Delete(Source)
                   
                   
            elif (Action.lower() == "rename"):                 # RENAME
                NewName = Path.Path(CDict['New_Name'])

                if Source.is_file():
                    File.Rename(Source,NewName)
                
                else :
                   Dir.Rename(Source,NewName)
            
            elif(Action.lower() == 'copy'):                    # COPY
                Des = Path.Path(CDict['Destination'])

                if Source.is_file():
                    File.copy(Source,Des)
                
                else :
                   Dir.Copy(Source,Des)
            
            elif (Action.lower() == 'move'):                   # MOVE
                Des = Path.Path(CDict['Destination'])

                if Source.is_file():
                    File.Move(Source,Des)
                
                else :
                   Dir.Move(Source,Des)
            
            elif (Action.lower() == 'create'):                        # CREATE
                Lowercommand: str = Command.lower()
                if ('dir' in Lowercommand or 'folder' in Lowercommand):
                    Source.mkdir()
                    print(f"{Source.name} Directory Created")
                    
                else:
                    Source.touch()
                    print(f"{Source.name} File Created")
            
            elif (Action.lower() == 'clear'):                       # CLEAR CONTENT
                File.ClearContent(Source)
            
            elif (Action.lower() == 'show'):                        # SHOW 
                Lowercommand: str = Command.lower()
                if ('content' in Lowercommand or Source.is_file()):
                    File.ShowContent(Source)
                else:
                    Dir.Show(Source)
            
            elif (Action.lower() == 'ch'):                          # CD 
                Sys.CD(Source)
            

            elif (Action.lower() == 'cwd' or Action.lower() == 'pwd'):      # CWD
                Sys.CWD()
            
            elif ('space' in Action.lower() or 'disk' in Action.lower()):    # DISK SPACE
                Sys.DiskSpace(Source)

            elif (Action.lower() in 'time'):                        # TIME
                Sys.Time()


            elif (Action.lower() == 'search'):
                Des = Path.Path(CDict['Destination'])
                if (Source.is_dir()):
                    search.SearchFile(CDict['Text'],Source)
                
                    
            




                
        
    
    except Exception as e:

        print("error: ",e)

    c = time.time()
    print(f"{c-b:.2f}")
    b=c
    