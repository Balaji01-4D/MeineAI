import time
a=time.time()
print(f'{a-0.0000:.2f}')
import re
import os
import spacy
import Actions as op
file = op.File()
nlp = spacy.load('/home/balaji/MeineAI/summaMeineAI')
b=time.time()
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
            CDict: dict = {}
            # Display the entities found in the text
            print(f"Input Text: {Command}")
            print("Entities Detected:")
            for ent in doc.ents:
                print(f" - {ent.text} ({ent.label_})")
                CDict[ent.label_] = ent.text
            # print(CDict)
            print(CDict['Action'],'delete')
            if (CDict['Action'] == "delete"):
               file.Delete(CDict['FIle_FolderName'])
            elif (CDict['Action'] == "rename"):
                        file.Delete(CDict['FIle_FolderName'])

        
    
    except Exception as e:

        print("error: ",e)

    c = time.time()
    print(f"{c-b:.2f}")
    b=c
    