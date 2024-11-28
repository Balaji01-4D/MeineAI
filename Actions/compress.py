import zipfile as zp
import shutil as sl
from pathlib import Path

class Zip:



    def Compress(self, Source: Path):
        try:
            if (not Source.exists()):
                print(f"{Source.name} Is Not Found.")
            elif (Source.exists() and not Source.is_dir()):
                    with zp.ZipFile(str(Source)+".zip","w",zp.ZIP_DEFLATED) as zipf:
                        zipf.write(Source,arcname=Source)
                        Source.unlink()
                        print(f"{Source.name} Compressed Successfully")
            elif (Source.is_dir()):
                    sl.make_archive(Source,'zip',Source.resolve().parent)
                    print(f"{Source.name} Compress Successfully")
        except Exception:
            print(f"Error in compressing the {Source.name}")


    def Extract(self, Source: Path) -> None:
        if (Source.exists()):
            print(f"{Source.name} Is Already in {Source.parent.name} Directory")
        else:
            try:
                StrSource = str(Source)
                if ('.zip' not in StrSource):
                    StrSource += '.zip'
                    Source = Path(StrSource)
                if (Source.exists()):
                    sl.unpack_archive(Source)
                    print(f"{Source.stem} Extracted Successfully")
                else:
                    print(f"{Source.stem} Not Found .")
            except Exception as e:
                print(f"Error In Extracting {Source.name} e.",e)
    
    def list_zip_contents(self, zip_file: Path):
        try:

            if not zip_file.exists():
                print(f"{zip_file.name} not found.")
                return
            elif not zip_file.suffix == ".zip":
                print(f"{zip_file.name} is not a valid zip file.")
                return
            with zp.ZipFile(zip_file, 'r') as zf:
                print(f"Contents of {zip_file.name}:\n")
                for file in zf.infolist():
                    file_type = "Folder" if file.is_dir() else "File"
                    print(f"{file.filename} - {file_type}")
        except Exception as e:
            print(f"Error listing contents of {zip_file.name}: {e}")




    


a = Zip()
p = Path('/home/balaji/Downloads/3dicons-png-dynamic-1.0.0.zip')
# a.list_zip_contents(p)