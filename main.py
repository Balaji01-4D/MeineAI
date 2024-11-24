import re
import os
import spacy
from operations.file import File

nlp = spacy.load('/home/balaji/MeineAI/MeineAI')
while True:
    Command: str = input(">>> ")
    try:
    
        if (re.fullmatch(r"[0-9+\-*/%(). ]+",Command)):
            print(eval(Command))

        elif bool(re.search(r"\b[sS]hell\b",Command)):
            sys:str = re.sub(r"\b[sS]hell\b","",Command)
            print("system command",sys)
            os.system(sys)
        


        else :
            doc = nlp(Command)
            CDict: dict = {}
            # Display the entities found in the text
            print(f"Input Text: {Command}")
            print("Entities Detected:")
            for ent in doc.ents:
                print(f" - {ent.text} ({ent.label_})")
                CDict[ent.label_] = ent.text
            print(CDict)
            # if (CDict['Action'] == 'delete'):
            #     File.Delete(CDict['File_FolderName'])

        
    
    except Exception as e:
        print(e)