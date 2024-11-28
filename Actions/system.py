import os
import datetime as dt
import shutil as sl
from pathlib import Path
from time import ctime
import psutil
from rich.console import Console
import platform
from tabulate import tabulate

console = Console()

from Actions import other
class System:

    def Time(self) -> None :
        print(dt.datetime.now())
    
    def DiskSpace(self, Destination: Path =Path('/')) -> None: 
        total , used , free = sl.disk_usage(Destination)
        data ={
            'FREE' : free / total * 100,
            'USED' : used / total * 100
        }
        other.display_progress(data,'Disk Space')
        print("Total :",other.SizeHelper(total))
        print("Used  :",other.SizeHelper(used))
        print("Free  :",other.SizeHelper(free))
    
    def GetCurrentDir(self) -> None:
        path:Path = Path('.')
        print(f"{path.resolve()}")


    def CD(self, Destination: Path) -> None:
        if (Destination.exists() and Destination.is_dir()):
            try:
                os.chdir(Path)
            except PermissionError:
                print(f"Permission Denied")            
            except Exception:
                print(f"Can't Change directory to {Destination.name}")
        elif (Destination.is_file()):
            print(f"Cant Change {Destination.name} Is File.")
        else:
            print(f"{Destination.name} Not Found.")
    def Info(self, Name : Path) -> None:
        if (not Name.exists()):
            print(f"{Name.name} Not Found")
            return
        size = other.SizeHelper(Name.stat().st_size) 
        stats = Name.stat()
        info : dict ={
            'Name' : Name.name,
            'Path' : str(Name.resolve()),
            'size' : size,
            'Type' : "File" if (not Name.is_dir()) else "Directory",
            'Created' : ctime(stats.st_ctime),
            'Last Modified' : ctime(stats.st_mtime),
            'Last Accessed' : ctime(stats.st_atime),
            'Mode' : stats.st_mode
        }
        for key,value in info.items():
            print(f"{key} : {value}")
    
    def IP(self):
        import socket
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        net_info = [
            ["Hostname", hostname],
            ["IP Address", ip_address],
        ]
        console.print(tabulate(net_info, headers=["Attribute", "Value"], tablefmt="fancy_grid"))

    
    def HomeDir(self):
        print(f"Home Directory :  ",Path.home())

    def RAMInfo(self):
        memory = psutil.virtual_memory()
        Total = memory.total
        Avail = memory.available
        Used = memory.used
        data: dict = { 
                'AVAILABLE': Avail/Total * 100,
                'USED' : Used/Total * 100
        }
        other.display_progress(data,'Ram Info')
        print(f"Total Memory : {other.SizeHelper(Total)}")
        print(f"Memory Available : {other.SizeHelper(Avail)}")
        print(f"Memory Used : {other.SizeHelper(Used)}")

    def SYSTEM(self):
        os_info = [
        ["System", platform.system()],
        ["Node Name", platform.node()],
        ["Release", platform.release()],
        ["Version", platform.version()],
        ["Machine", platform.machine()],
        ["Processor", platform.processor()],
        ]
        console.print("\n[OS Information]")
        console.print(tabulate(os_info, headers=["NAME", "INFO"], tablefmt="fancy_grid"))

    def Battery(self):
        battery = psutil.sensors_battery()
        if battery:
            other.display_progress({'BATTERY %': round(battery.percent)},'BATTERY')
            console.print(f"[blue]Battery Status: {'Charging' if battery.power_plugged else "Not Charging"}")
        else:
            console.print(f"[blue]No battery information available.")


    def NetWork(self):
        net_info = psutil.net_if_addrs()
        for interface, addresses in net_info.items():
            console.print(f"[blue]Interface: {interface}")
            for address in addresses:
                console.print(f" [blue]Address: {address.address}, Family: {address.family.name}")
            
    def ENV(self):
        env_vars = os.environ
        for key, value in env_vars.items():
            console.print(f"{key}: {value}")

                

    def CPU(self):
        console.print(f"[blue]CPU Count: {psutil.cpu_count(logical=True)}")
        console.print(f"[blue]CPU Usage: {psutil.cpu_percent(interval=1)}%")

    def USER(self):
        import getpass
        console.print(f"[blue]Current User: {getpass.getuser()}")

    def DiskInfo(self):
        disk_info = []
        seen_devices = set()  
        for partition in psutil.disk_partitions():
            if partition.device not in seen_devices:  
                usage = psutil.disk_usage(partition.mountpoint)
                disk_info.append([
                    partition.device,
                    f"{usage.total / (1024 ** 3):.2f} GB",
                    f"{usage.used / (1024 ** 3):.2f} GB",
                    f"{usage.free / (1024 ** 3):.2f} GB",
                    f"{usage.percent}%",
                ])
                seen_devices.add(partition.device)  

        console.print(tabulate(disk_info, headers=["Device", "Total Size", "Used", "Free", "Usage"], tablefmt="fancy_grid"))          

