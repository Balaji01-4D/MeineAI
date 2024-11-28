from pathlib import Path 

def SizeHelper(Size : int) -> None:
    for unit in ['B','KB','MB','GB']:
        if (Size < 1024):
            return f"{Size:.2f} {unit}"
        Size/=1024

def Is_subsequence(Sub: str,Main: str) -> None:
    it=iter(Main)
    return all(item in it for item in Sub)


def CMDMapper(labels: list[str],text: list[str]):
    cdict = {}
    Backup = {'FILE':'NEWNAME','FOLDER':'DESTINATION'}
    for label,val in zip(labels,text):
        if (cdict.__contains__(label)):
            cdict[Backup[label]] = val
        else :
            cdict[label] = val
    return cdict