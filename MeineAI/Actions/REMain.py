import re
from pathlib import Path
import Actions.prime as prime
d = {
    'twopath':r'(move|mv|m|push|cp|c|copy)\s+(?:the)?(?:\s+(?:folder|file))?\s+([^\s]+)\s+to(?:\s+folder)?\s*(\/?[^\s]*)?',
    'onepath':r"(delete|d|rm|remove|r|del)\s*(?:the)?(?:\s+(folder|file))?\s+([^\s]+)",
    'rename':r'(rename|rn)\s*(?:the\s*)?(?:file|folder)?\s+([^\s]+)\s(?:as|to)\s([^\n\s]+)',
    'create':r'(mk|make|create|mkdir|info)\s*(?:the)?(?:\s+(folder|file))?\s+([^\s]+)',
    'system':r'(battery|bt|charge|my ram|user|me|env|envirnoment variable|ip|cpu|disk|ram|network|time|sys|system info|info|ls|cpu|network|disk|storage|network info|)'
    }

def CLI():
    while True:
        Command: str = input('>>> ')
        CDict: dict[str] = {}
    
        if (re.fullmatch(d['onepath'],Command)):
            Match = re.match(d['onepath'],Command)
            CDict['ACTION'] = Match.group(1)
            if (Match.group)(2):
                CDict['HINT'] = Match.group(2)
            CDict['FILE'] = Match.group(3)


        if (re.fullmatch(d['create'],Command)):
            Match = re.match(d['create'],Command)
            CDict['ACTION'] = Match.group(1)
            if (Match.group)(2):
                CDict['HINT'] = Match.group(2)
            CDict['FILE'] = Match.group(3)

        
        elif (re.fullmatch(d['twopath'],Command)):
            Match = re.match(d['twopath'],Command)
            CDict['ACTION'] = Match.group(1)
            Unknown = Path(Match.group(2))
            if (Unknown.is_dir()):
                CDict['FOLDER'] = Unknown.resolve()
                CDict['DESTINATION'] = Match.group(3)
            elif (not Unknown.exists()):
                print('Source not found')
            else :
                CDict['FILE'] = Unknown.resolve()
                CDict['FOLDER'] = Match.group(3)



        elif (re.fullmatch(d['rename'],Command)):
            Match = re.match(d['rename'],Command)
            CDict['ACTION'] = Match.group(1)
            Unknown = Path(Match.group(2))
            if (Unknown.is_dir()):
                CDict['FOLDER'] = Unknown.resolve()
                CDict['NEWNAME'] = Match.group(3)
            elif (not Unknown.exists()):
                print('Source not found')
            else :
                CDict['FILE'] = Unknown.resolve()
                CDict['NEWNAME'] = Match.group(3)
            
        
        elif(re.fullmatch(d['system'],Command)):
            Match = re.match(d['system'],Command)
            CDict['ACTION'] = Match.group(1)

        print(CDict)
        if (CDict.__contains__('ACTION')):
            prime.WHatAction(CDict['ACTION'],CDict)
        else:
            print('CANNOT CAPTURE THE ACTION')

CLI()