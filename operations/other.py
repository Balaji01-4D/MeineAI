def SizeHelper(Size : int) -> None:
    for unit in ['B','KB','MB','GB']:
        if (Size < 1024):
            return f"{Size:.2f} {unit}"
        Size/=1024

def Is_subsequence(Sub: str,Main: str) -> None:
    it=iter(Main)
    return all(item in it for item in Sub)
# import time 0.072126