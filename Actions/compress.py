import zipfile as zp
import shutil as sl

class Zip:
    def ZipFile(self,Source: str) -> None:
        try:
            with zp.ZipFile(Source+".zip","w",zp.ZIP_DEFLATED) as zipf:
                zipf.write(Source,arcname=Source)
                print("Compress Successfully")
        except Exception as e:
            print(e)

    def ZipFolder(self,Source: str) -> None:
        try:
            sl.make_archive(Source,'zip',Source)
            print("Compress Successfully")
        except Exception as e:
            print(e)
    
    def ExtractFolder(self,Source: str) -> None:
        try:
            sl.unpack_archive(Source)
            print("Extracted Successfully")
        except Exception as e:
            print(e)

    def ZipShow(self,Source: str) -> None:
        try:
            if ('.zip' not in Source):
                Source += '.zip'           
            with zp.ZipFile(Source,'r') as zipf:
                print(zipf.namelist())
        except Exception as e:
            print(e)
    
    def SelectExtract(self,Source: str,*Files: tuple[str]) -> None:
        try:
            with zp.ZipFile(Source,'r') as zipf:
                for file in Files:
                    if (file in zipf.namelist()):
                        zipf.extract(file)
                        print(f"{file} Extracted Successfully")
                    else:
                        print(f"{file} Not Found")
        except Exception as e:

            print(e)
