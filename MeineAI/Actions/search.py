import subprocess as sp
import os

class Search:

    def SearchFile(self, FileName: str, Path: str='.') -> None:
        def SearchHelper(FileName: str,Path: str) -> str|None:
            l:list[str]=[]
            try:
                for root,dirs,files in os.walk(Path):
                    if (FileName in files):
                        l.append(os.path.join(root,FileName))
                return l
            except Exception:
                print("Error occurs searching the file")

        Result = SearchHelper(FileName,Path)
        if (Result):
            for paths in Result:
                print("File Found -> ",paths)
        else:
            print("File Not Found")
    
    def SearchFolder(self,FolderName:str,Path:str='.') -> None:
        def SearchHelper(FolderName: str,Path: str) -> list[str]:
            l:list[str]=[]
            try:
                for root,dirs,files in os.walk(Path):
                    if (FolderName in dirs):
                        l.append(os.path.join(root,FolderName))
                return l
            except Exception:
                print("Error occur in searching Directory")

        Result = SearchHelper(FolderName,Path)
        if (Result):
            for paths in Result:
                print("Folder Found -> ",paths)
        else:
            print("Folder Not Found")
            
    def TextFinderInFile(self,Text: str,Path: str='.') -> None:
        '''
        Only for Linux and mac
        '''
        try:
            sp.run(['grep','-Rl',Text,Path])                      #Linux
        except Exception as e:
            print(e)

    def TextFinderFile(self,Text: str,Path: str='.') -> None:              #slow but all os
        '''
        Slower for large tree 
        supports all os
        '''
        def Helper(Text:str,path:str) -> list[str]:
            matching_files=[]
            for root,dir,files in os.walk(Path):
                for file in files:
                    file_path = os.path.join(root,file)
                    try:
                        with open(file_path,'r',encoding='utf-8') as f:
                            for line_num,line in enumerate(f,start=1):
                                if (Text in line):
                                    matching_files.append((file_path,line_num))
                    except (UnicodeDecodeError,IOError):
                        continue
            return matching_files
        
        Result = Helper(Text,Path)
        if (Result):
            for paths,line_num in Result:
                print(f"Text Found @ {line_num} Line -> {paths.replace('./',os.getcwd()+'/')}")
        else:
            print("Text Not Found")

